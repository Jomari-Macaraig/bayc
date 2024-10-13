import time

from .base import BAYCBaseCommand
from ...tasks import process_bayc_transfer_events


class Command(BAYCBaseCommand):
    help = "Process past events for BAYC Transfer Events"

    def add_arguments(self, parser):
        parser.add_argument("--from_block", action="store", type=int, required=True)
        parser.add_argument("--to_block", action="store", type=int, required=True)

    def handle(self, *args, **options):

        from_block = options["from_block"]
        to_block = options["to_block"]

        self.stdout.write(
            self.style.SUCCESS(f"Processing events from block {from_block} to block {to_block}")
        )
        smart_contract = self.get_smart_contract()
        events = smart_contract.events.Transfer.create_filter(
            from_block=from_block, to_block=to_block
        ).get_all_entries()
        process_bayc_transfer_events.apply_async(kwargs={"events": self.serialize_events(events=events)})
