"""
Everything in this file is what Vulture found as dead code but either isn't really
dead or is kept deliberately. Referencing these in a file like this makes sure that
Vulture doesn't mark these as dead again.
"""
from infection_monkey.exploit.log4shell_utils.ldap_server import LDAPServerFactory
from monkey_island.cc import app
from monkey_island.cc.models import Report

fake_monkey_dir_path  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:37)
set_os_linux  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:37)
fake_monkey_dir_path  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:57)
set_os_windows  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:57)
fake_monkey_dir_path  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:77)
set_os_linux  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:77)
fake_monkey_dir_path  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:92)
set_os_windows  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:92)
fake_monkey_dir_path  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:107)
set_os_linux  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:107)
fake_monkey_dir_path  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:122)
set_os_windows  # unused variable (monkey/tests/infection_monkey/post_breach/actions/test_users_custom_pba.py:122)
patch_new_user_classes  # unused variable (monkey/tests/infection_monkey/utils/test_auto_new_user_factory.py:25)
patch_new_user_classes  # unused variable (monkey/tests/infection_monkey/utils/test_auto_new_user_factory.py:31)
custom_pba_directory  # unused variable (monkey/tests/monkey_island/cc/services/test_post_breach_files.py:20)
configure_resources  # unused function (monkey/tests/monkey_island/cc/environment/test_environment.py:26)
change_to_mongo_mock  # unused function (monkey/monkey_island/cc/test_common/fixtures/mongomock_fixtures.py:9)
uses_database  # unused function (monkey/monkey_island/cc/test_common/fixtures/mongomock_fixtures.py:16)
datas  # unused variable (monkey/monkey_island/pyinstaller_hooks/hook-stix2.py:9)
test_key  # unused variable (monkey/monkey_island/cc/services/zero_trust/zero_trust_report/finding_service.py:20)
pillars  # unused variable (monkey/monkey_island/cc/services/zero_trust/zero_trust_report/finding_service.py:21)
CLEAN_UNKNOWN  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:9)
CLEAN_LINUX  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:10)
CLEAN_WINDOWS  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:11)
EXPLOITED_LINUX  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:12)
EXPLOITED_WINDOWS  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:13)
ISLAND_MONKEY_LINUX  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:15)
ISLAND_MONKEY_LINUX_RUNNING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:16)
ISLAND_MONKEY_LINUX_STARTING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:17)
ISLAND_MONKEY_WINDOWS  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:18)
ISLAND_MONKEY_WINDOWS_RUNNING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:19)
ISLAND_MONKEY_WINDOWS_STARTING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:20)
MANUAL_LINUX  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:21)
MANUAL_LINUX_RUNNING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:22)
MANUAL_WINDOWS  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:23)
MANUAL_WINDOWS_RUNNING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:24)
MONKEY_LINUX  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:25)
MONKEY_WINDOWS  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:27)
MONKEY_WINDOWS_RUNNING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:28)
MONKEY_WINDOWS_STARTING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:29)
MONKEY_LINUX_STARTING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:30)
_.credential_type  # unused attribute (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/processors/cred_exploit.py:19)
_.credential_type  # unused attribute (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/processors/cred_exploit.py:22)
_.credential_type  # unused attribute (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/processors/cred_exploit.py:25)
_.password_restored  # unused attribute (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/processors/zerologon.py:11)
credential_type  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_report_info.py:18)
password_restored  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_report_info.py:23)
SSH  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:30)
SAMBACRY  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:31)
ELASTIC  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:32)
STRUTS2  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:39)
WEBLOGIC  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:40)
HADOOP  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:43)
MSSQL  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:44)
VSFTPD  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:45)
DRUPAL  # unused variable (monkey/monkey_island/cc/services/reporting/issue_processing/exploit_processing/exploiter_descriptor_enum.py:48)
POWERSHELL  # (\monkey\monkey_island\cc\services\reporting\issue_processing\exploit_processing\exploiter_descriptor_enum.py:52)
ExploiterDescriptorEnum.LOG4SHELL
PbaResults  # unused class (monkey/monkey_island/cc/models/pba_results.py:4)
internet_access  # unused variable (monkey/monkey_island/cc/models/monkey.py:43)
config_error  # unused variable (monkey/monkey_island/cc/models/monkey.py:53)
pba_results  # unused variable (monkey/monkey_island/cc/models/monkey.py:55)
launch_time  # unused variable (monkey/monkey_island/cc/models/monkey.py)
command_control_channel  # unused variable (monkey/monkey_island/cc/models/monkey.py:58)
meta  # unused variable (monkey/monkey_island/cc/models/zero_trust/finding.py:37)
meta  # unused variable (monkey/monkey_island/cc/models/monkey_ttl.py:34)
expire_at  # unused variable (monkey/monkey_island/cc/models/monkey_ttl.py:36)
meta  # unused variable (monkey/monkey_island/cc/models/config.py:11)
meta  # unused variable (monkey/monkey_island/cc/models/creds.py:9)
meta  # unused variable (monkey/monkey_island/cc/models/edge.py:5)
Config  # unused class (monkey/monkey_island/cc/models/config.py:4)
Creds  # unused class (monkey/monkey_island/cc/models/creds.py:4)
_.do_CONNECT  # unused method (monkey/infection_monkey/transport/http.py:151)
_.do_POST  # unused method (monkey/infection_monkey/transport/http.py:122)
_.do_HEAD  # unused method (monkey/infection_monkey/transport/http.py:61)
_.do_GET  # unused method (monkey/infection_monkey/transport/http.py:38)
_.do_POST  # unused method (monkey/infection_monkey/transport/http.py:34)
_.do_GET  # unused method (monkey/infection_monkey/exploit/weblogic.py:237)
PowerShellExploiter  # (monkey\infection_monkey\exploit\powershell.py:27)
ElasticFinger  # unused class (monkey/infection_monkey/network/elasticfinger.py:18)
HTTPFinger  # unused class (monkey/infection_monkey/network/httpfinger.py:9)
MySQLFinger  # unused class (monkey/infection_monkey/network/mysqlfinger.py:13)
SSHFinger  # unused class (monkey/infection_monkey/network/sshfinger.py:15)
ClearCommandHistory  # unused class (monkey/infection_monkey/post_breach/actions/clear_command_history.py:11)
AccountDiscovery  # unused class (monkey/infection_monkey/post_breach/actions/discover_accounts.py:8)
ModifyShellStartupFiles  # unused class (monkey/infection_monkey/post_breach/actions/modify_shell_startup_files.py:11)
Timestomping  # unused class (monkey/infection_monkey/post_breach/actions/timestomping.py:6)
SignedScriptProxyExecution  # unused class (monkey/infection_monkey/post_breach/actions/use_signed_scripts.py:15)
EnvironmentCollector  # unused class (monkey/infection_monkey/system_info/collectors/environment_collector.py:19)
HostnameCollector  # unused class (monkey/infection_monkey/system_info/collectors/hostname_collector.py:10)
_.coinit_flags  # unused attribute (monkey/infection_monkey/system_info/windows_info_collector.py:11)
_.representations  # unused attribute (monkey/monkey_island/cc/app.py:180)
_.log_message  # unused method (monkey/infection_monkey/transport/http.py:188)
_.log_message  # unused method (monkey/infection_monkey/transport/http.py:109)
_.version_string  # unused method (monkey/infection_monkey/transport/http.py:148)
_.version_string  # unused method (monkey/infection_monkey/transport/http.py:27)
_.close_connection  # unused attribute (monkey/infection_monkey/transport/http.py:57)
protocol_version  # unused variable (monkey/infection_monkey/transport/http.py:24)
binaries  # unused variable (monkey/infection_monkey/pyinstaller_hooks/hook-pypsrp.py:3)
hiddenimports  # unused variable (monkey/infection_monkey/pyinstaller_hooks/hook-infection_monkey.exploit.py:3)
hiddenimports  # unused variable (monkey/infection_monkey/pyinstaller_hooks/hook-infection_monkey.network.py:3)
hiddenimports  # unused variable (monkey/infection_monkey/pyinstaller_hooks/hook-infection_monkey.post_breach.actions.py:4)
hiddenimports  # unused variable (monkey/infection_monkey/pyinstaller_hooks/hook-infection_monkey.system_info.collectors.py:4)
_.wShowWindow  # unused attribute (monkey/infection_monkey/monkey.py:345)
_.dwFlags  # unused attribute (monkey/infection_monkey/monkey.py:344)
_.do_get  # unused method (monkey/infection_monkey/exploit/zerologon_utils/remote_shell.py:79)
_.do_exit  # unused method (monkey/infection_monkey/exploit/zerologon_utils/remote_shell.py:96)
_.prompt  # unused attribute (monkey/infection_monkey/exploit/zerologon_utils/remote_shell.py:108)
_.prompt  # unused attribute (monkey/infection_monkey/exploit/zerologon_utils/remote_shell.py:125)
keytab  # unused variable (monkey/infection_monkey/exploit/zerologon_utils/options.py:16)
no_pass  # unused variable (monkey/infection_monkey/exploit/zerologon_utils/options.py:18)
ts  # unused variable (monkey/infection_monkey/exploit/zerologon_utils/options.py:25)
opnum  # unused variable (monkey/infection_monkey/exploit/zerologon.py:466)
structure  # unused variable (monkey/infection_monkey/exploit/zerologon.py:467)
structure  # unused variable (monkey/infection_monkey/exploit/zerologon.py:478)
oid_set  # unused variable (monkey/infection_monkey/exploit/tools/wmi_tools.py:96)
export_monkey_telems  # unused variable (monkey/infection_monkey/config.py:282)
NoInternetError  # unused class (monkey/common/utils/exceptions.py:33)
_.__isabstractmethod__  # unused attribute (monkey/common/utils/code_utils.py:11)
MIMIKATZ  # unused variable (monkey/common/utils/attack_utils.py:21)
MIMIKATZ_WINAPI  # unused variable (monkey/common/utils/attack_utils.py:25)
DROPPER  # unused variable (monkey/common/utils/attack_utils.py:29)
pytest_addoption  # unused function (envs/os_compatibility/conftest.py:4)
pytest_addoption  # unused function (envs/monkey_zoo/blackbox/conftest.py:4)
pytest_runtest_setup  # unused function (envs/monkey_zoo/blackbox/conftest.py:47)
config_value_list  # unused variable (envs/monkey_zoo/blackbox/config_templates/smb_pth.py:10)
ALIBABA  # unused variable (monkey/common/cloud/environment_names.py:10)
IBM  # unused variable (monkey/common/cloud/environment_names.py:11)
DigitalOcean  # unused variable (monkey/common/cloud/environment_names.py:12)
_.aws_info  # unused attribute (monkey/monkey_island/cc/environment/aws.py:13)
build_from_config_file_contents  # unused method 'build_from_config_file_contents' (\monkey_island\setup\island_config_options.py:18)
mock_port_in_env_singleton  # monkey\tests\unit_tests\monkey_island\cc\services\test_config.py:26:
ISLAND  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:14)
MONKEY_LINUX_RUNNING  # unused variable (monkey/monkey_island/cc/services/utils/node_states.py:26)
import_status  # monkey_island\cc\resources\configuration_import.py:19
config_schema  # monkey_island\cc\resources\configuration_import.py:25
exception_stream  # unused attribute (monkey_island/cc/server_setup.py:104)
ADVANCED  # unused attribute (monkey/monkey_island/cc/services/mode/mode_enum.py:6:)
Report.overview
Report.recommendations
Report.glance
Report.meta_info
Report.meta
LDAPServerFactory.buildProtocol

# these are not needed for it to work, but may be useful extra information to understand what's going on
WINDOWS_PBA_TYPE  # unused variable (monkey/monkey_island/cc/resources/pba_file_upload.py:23)
WINDOWS_TTL  # unused variable (monkey/infection_monkey/network/ping_scanner.py:17)
wlist  # unused variable (monkey/infection_monkey/transport/tcp.py:28)
wlist  # unused variable (monkey/infection_monkey/transport/http.py:176)
charset  # unused variable (monkey/infection_monkey/network/mysqlfinger.py:81)
salt  # unused variable (monkey/infection_monkey/network/mysqlfinger.py:78)
thread_id  # unused variable (monkey/infection_monkey/network/mysqlfinger.py:61)


# leaving this since there's a TODO related to it
_.get_wmi_info  # unused method (monkey/infection_monkey/system_info/windows_info_collector.py:63)


# potentially unused (there may also be unit tests referencing these)
LOG_DIR_NAME  # unused variable (envs/monkey_zoo/blackbox/log_handlers/test_logs_handler.py:8)
delete_logs  # unused function (envs/monkey_zoo/blackbox/test_blackbox.py:85)
MongoQueryJSONEncoder  # unused class (envs/monkey_zoo/blackbox/utils/json_encoder.py:6)
environment  # unused variable (monkey/monkey_island/cc/models/monkey.py:59)
_.environment  # unused attribute (monkey/monkey_island/cc/services/telemetry/processing/system_info_collectors/environment.py:10)
_.instance_name  # unused attribute (monkey/common/cloud/azure/azure_instance.py:35)
_.instance_name  # unused attribute (monkey/common/cloud/azure/azure_instance.py:64)
GCPHandler  # unused function (envs/monkey_zoo/blackbox/test_blackbox.py:57)

# TODO: Reevaluate these as the agent refactor progresses
run_sys_info_collector
ping
scan_tcp_port
fingerprint
interrupt
MockPuppet
ControlChannel
should_agent_stop
get_credentials_for_propagation
MockMaster
register_signal_handlers
