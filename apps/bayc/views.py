from rest_framework.generics import ListAPIView

from .models import BAYCTransferEvent
from .serializers import BAYCTransferEventSerializer


class BAYCTransferEventListAPIView(ListAPIView):
    serializer_class = BAYCTransferEventSerializer

    def get_queryset(self):
        token_id = self.kwargs.get("token_id")
        queryset = BAYCTransferEvent.objects.all()
        if token_id:
            queryset = queryset.filter(token_id=token_id)
        return queryset
