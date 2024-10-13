import json

from django.conf import settings
from django.core.management.base import BaseCommand
from web3 import Web3

from ...exceptions import InfuraConnectionFailed


class BAYCBaseCommand(BaseCommand):
    help = "Base Command for BAYC"

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

    def serialize_events(self, events):
        serialized_events = []
        for event in events:
            serialized_events.append({
                "token_id": event.args["tokenId"],
                "from_address": Web3.to_checksum_address(event.args["from"]),
                "to_address": Web3.to_checksum_address(event.args["to"]),
                "transaction_hash": event["transactionHash"].to_0x_hex(),
                "block_number": event["blockNumber"],
            })
        return serialized_events