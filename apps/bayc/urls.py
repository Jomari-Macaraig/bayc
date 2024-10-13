from django.urls import path

from .views import BAYCTransferEventListAPIView

urlpatterns = [
    path("", BAYCTransferEventListAPIView.as_view()),
    path("<int:token_id>", BAYCTransferEventListAPIView.as_view()),
]