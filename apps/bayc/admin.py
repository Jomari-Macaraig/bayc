from django.contrib import admin

from .models import BAYCTransferEvent


class BAYCTransferEventAdmin(admin.ModelAdmin):
    list_display = (
        "token_id",
        "from_address",
        "to_address",
        "transaction_hash",
        "block_number",
    )


admin.site.register(BAYCTransferEvent, BAYCTransferEventAdmin)
