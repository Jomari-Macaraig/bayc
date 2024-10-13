from rest_framework import serializers

from .models import BAYCTransferEvent


class BAYCTransferEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BAYCTransferEvent
        fields = (
            "token_id",
            "from_address",
            "to_address",
            "transaction_hash",
            "block_number"
        )
