import time
import json
from web3 import Web3

from django.core.management.base import BaseCommand
from django.conf import settings

from ...exceptions import InfuraConnectionFailed
from ...tasks import process_bayc_transfer_events


class Command(BaseCommand):
    help = "Listen for BAYC Transfer Events"

    @staticmethod
    def get_infura_endpoint():
        return f"{settings.INFURA_URI}{settings.INFURA_API_KEY}"

    def get_provider(self):
        w3 = Web3(Web3.HTTPProvider(self.get_infura_endpoint()))
        return w3

    @staticmethod
    def get_abi():
        with open(settings.ABI_FILE) as f:
            abi = json.load(f)
        return abi

    def get_smart_contract(self):
        w3 = self.get_provider()

        if not w3.is_connected():
            raise InfuraConnectionFailed("Infura connection failed, please check configuration")

        abi = self.get_abi()
        contract_address = w3.to_checksum_address(settings.BAYC_CONTRACT_ADDRESS)
        smart_contract = w3.eth.contract(address=contract_address, abi=abi)

        return smart_contract

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Listening for events")
        )
        smart_contract = self.get_smart_contract()
        events = smart_contract.events.Transfer.create_filter(from_block="latest")
        while True:
            process_bayc_transfer_events(events=events.get_new_entries())
            time.sleep(3)