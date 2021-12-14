import logging
from queue import Queue
from threading import Event
from typing import Dict

from infection_monkey.i_puppet import (
    ExploiterResultData,
    FingerprintData,
    PingScanData,
    PortScanData,
    PortStatus,
)
from infection_monkey.model import VictimHost, VictimHostFactory
from infection_monkey.telemetry.exploit_telem import ExploitTelem
from infection_monkey.telemetry.messengers.i_telemetry_messenger import ITelemetryMessenger
from infection_monkey.telemetry.scan_telem import ScanTelem

from . import Exploiter, IPScanner, IPScanResults
from .threading_utils import create_daemon_thread

logger = logging.getLogger()


class Propagator:
    def __init__(
        self,
        telemetry_messenger: ITelemetryMessenger,
        ip_scanner: IPScanner,
        exploiter: Exploiter,
        victim_host_factory: VictimHostFactory,
    ):
        self._telemetry_messenger = telemetry_messenger
        self._ip_scanner = ip_scanner
        self._exploiter = exploiter
        self._victim_host_factory = victim_host_factory
        self._hosts_to_exploit = None

    def propagate(self, propagation_config: Dict, stop: Event):
        logger.info("Attempting to propagate")

        network_scan_completed = Event()
        self._hosts_to_exploit = Queue()

        scan_thread = create_daemon_thread(
            target=self._scan_network, args=(propagation_config, stop)
        )
        exploit_thread = create_daemon_thread(
            target=self._exploit_hosts,
            args=(propagation_config, network_scan_completed, stop),
        )

        scan_thread.start()
        exploit_thread.start()

        scan_thread.join()
        network_scan_completed.set()

        exploit_thread.join()

        logger.info("Finished attempting to propagate")

    def _scan_network(self, propagation_config: Dict, stop: Event):
        logger.info("Starting network scan")

        # TODO: Generate list of IPs to scan from propagation targets config
        ips_to_scan = propagation_config["targets"]["subnet_scan_list"]

        scan_config = propagation_config["network_scan"]
        self._ip_scanner.scan(ips_to_scan, scan_config, self._process_scan_results, stop)

        logger.info("Finished network scan")

    def _process_scan_results(self, ip: str, scan_results: IPScanResults):
        victim_host = self._victim_host_factory.build_victim_host(ip)

        Propagator._process_ping_scan_results(victim_host, scan_results.ping_scan_data)
        Propagator._process_tcp_scan_results(victim_host, scan_results.port_scan_data)
        Propagator._process_fingerprinter_results(victim_host, scan_results.fingerprint_data)

        if IPScanner.port_scan_found_open_port(scan_results.port_scan_data):
            self._hosts_to_exploit.put(victim_host)

        self._telemetry_messenger.send_telemetry(ScanTelem(victim_host))

    @staticmethod
    def _process_ping_scan_results(victim_host: VictimHost, ping_scan_data: PingScanData):
        victim_host.icmp = ping_scan_data.response_received
        if ping_scan_data.os is not None:
            victim_host.os["type"] = ping_scan_data.os

    @staticmethod
    def _process_tcp_scan_results(victim_host: VictimHost, port_scan_data: PortScanData) -> bool:
        for psd in port_scan_data.values():
            if psd.status == PortStatus.OPEN:
                victim_host.services[psd.service] = {}
                victim_host.services[psd.service]["display_name"] = "unknown(TCP)"
                victim_host.services[psd.service]["port"] = psd.port
                if psd.banner is not None:
                    victim_host.services[psd.service]["banner"] = psd.banner

    @staticmethod
    def _process_fingerprinter_results(victim_host: VictimHost, fingerprint_data: FingerprintData):
        for fd in fingerprint_data.values():
            # TODO: This logic preserves the existing behavior prior to introducing IMaster and
            #       IPuppet, but it is possibly flawed. Different fingerprinters may detect
            #       different os types or versions, and this logic isn't sufficient to handle those
            #       conflicts. Reevaluate this logic when we overhaul our scanners/fingerprinters.
            if fd.os_type is not None:
                victim_host.os["type"] = fd.os_type

            if ("version" not in victim_host.os) and (fd.os_version is not None):
                victim_host.os["version"] = fd.os_version

            for service, details in fd.services.items():
                victim_host.services.setdefault(service, {}).update(details)

    def _exploit_hosts(
        self,
        propagation_config: Dict,
        network_scan_completed: Event,
        stop: Event,
    ):
        logger.info("Exploiting victims")

        exploiter_config = propagation_config["exploiters"]
        self._exploiter.exploit_hosts(
            exploiter_config,
            self._hosts_to_exploit,
            self._process_exploit_attempts,
            network_scan_completed,
            stop,
        )

        logger.info("Finished exploiting victims")

    def _process_exploit_attempts(
        self, exploiter_name: str, host: VictimHost, result: ExploiterResultData
    ):
        if result.success:
            logger.info("Successfully propagated to {host} using {exploiter_name}")
        else:
            logger.info(
                f"Failed to propagate to {host} using {exploiter_name}: {result.error_message}"
            )

        self._telemetry_messenger.send_telemetry(
            ExploitTelem(exploiter_name, host, result.success, result.info, result.attempts)
        )
