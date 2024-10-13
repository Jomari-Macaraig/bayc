from django.db import models

from apps.base.models import Audit


class BAYCTransferEvent(Audit):
    token_id = models.IntegerField()
    from_address = models.CharField(max_length=42)
    to_address = models.CharField(max_length=42)
    transaction_hash = models.CharField(max_length=66)
    block_number = models.IntegerField()

    def __str__(self):
        return self.transaction_hash
