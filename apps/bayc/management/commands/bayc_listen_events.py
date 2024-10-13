import time

from .base import BAYCBaseCommand
from ...tasks import process_bayc_transfer_events


class Command(BAYCBaseCommand):
    help = "Listen for BAYC Transfer Events"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Listening for events")
        )
        smart_contract = self.get_smart_contract()
        events = smart_contract.events.Transfer.create_filter(from_block="latest")
        while True:
            self.stdout.write(
                self.style.SUCCESS("Processing events")
            )
            process_bayc_transfer_events.apply_async(
                kwargs={"events": self.serialize_events(events=events.get_new_entries())}
            )
            time.sleep(3)
