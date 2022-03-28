from unittest.mock import MagicMock

import pytest

from infection_monkey.credential_collectors import Password, SSHKeypair, Username
from infection_monkey.credential_store import AggregatingCredentialsStore
from infection_monkey.i_puppet import Credentials

DEFAULT_CREDENTIALS = {
    "exploit_user_list": ["Administrator", "root", "user1"],
    "exploit_password_list": ["123456", "123456789", "password", "root"],
    "exploit_lm_hash_list": ["aasdf23asd1fdaasadasdfas"],
    "exploit_ntlm_hash_list": ["asdfadvxvsdftw3e3421234123412", "qw4trklxklvznksbhasd1231"],
    "exploit_ssh_keys": [
        {"public_key": "some_public_key", "private_key": "some_private_key"},
        {
            "public_key": "ssh-ed25519 AAAAC3NzEIFaJ7xH+Yoxd\n",
            "private_key": "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BdHIAAAAGYXjl0j66VAKruPEKjS3A=\n"
            "-----END OPENSSH PRIVATE KEY-----\n",
        },
    ],
}


PROPAGATION_CREDENTIALS = {
    "exploit_user_list": ["user1", "user3"],
    "exploit_password_list": ["abcdefg", "root"],
    "exploit_ssh_keys": [{"public_key": "some_public_key", "private_key": "some_private_key"}],
}

TELEM_CREDENTIALS = [
    Credentials(
        [Username("user1"), Username("user3")],
        [
            Password("abcdefg"),
            Password("root"),
            SSHKeypair(public_key="some_public_key", private_key="some_private_key"),
        ],
    )
]


@pytest.fixture
def aggregating_credentials_store() -> AggregatingCredentialsStore:
    control_channel = MagicMock()
    control_channel.get_credentials_for_propagation.return_value = DEFAULT_CREDENTIALS
    return AggregatingCredentialsStore(control_channel)


def test_get_credentials_from_store(aggregating_credentials_store):
    aggregating_credentials_store.get_credentials()

    actual_stored_credentials = aggregating_credentials_store.stored_credentials

    assert (
        actual_stored_credentials["exploit_user_list"] == DEFAULT_CREDENTIALS["exploit_user_list"]
    )
    assert (
        actual_stored_credentials["exploit_password_list"]
        == DEFAULT_CREDENTIALS["exploit_password_list"]
    )
    assert (
        actual_stored_credentials["exploit_ntlm_hash_list"]
        == DEFAULT_CREDENTIALS["exploit_ntlm_hash_list"]
    )

    for ssh_keypair in actual_stored_credentials["exploit_ssh_keys"]:
        assert ssh_keypair in DEFAULT_CREDENTIALS["exploit_ssh_keys"]


def test_add_credentials_to_empty_store(aggregating_credentials_store):
    aggregating_credentials_store.add_credentials(TELEM_CREDENTIALS)

    assert aggregating_credentials_store.stored_credentials == PROPAGATION_CREDENTIALS


def test_add_credentials_to_full_store(aggregating_credentials_store):

    aggregating_credentials_store.get_credentials()

    aggregating_credentials_store.add_credentials(TELEM_CREDENTIALS)

    actual_stored_credentials = aggregating_credentials_store.stored_credentials

    assert actual_stored_credentials["exploit_user_list"] == [
        "Administrator",
        "root",
        "user1",
        "user3",
    ]
    assert actual_stored_credentials["exploit_password_list"] == [
        "123456",
        "123456789",
        "abcdefg",
        "password",
        "root",
    ]

    for ssh_keypair in actual_stored_credentials["exploit_ssh_keys"]:
        assert ssh_keypair in DEFAULT_CREDENTIALS["exploit_ssh_keys"]
