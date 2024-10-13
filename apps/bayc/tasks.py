from django.db import transaction

from .models import BAYCTransferEvent
from config.celery import app


@app.task(name="bayc.process_bayc_transfer_events")
@transaction.atomic()
def process_bayc_transfer_events(events):
    entries = []
    for event in events:
        entry = BAYCTransferEvent(
            token_id=event["token_id"],
            from_address=event["from_address"],
            to_address=event["to_address"],
            transaction_hash=event["transaction_hash"],
            block_number=event["block_number"],
        )
        entries.append(entry)
    if len(entries):
        BAYCTransferEvent.objects.bulk_create(entries)
