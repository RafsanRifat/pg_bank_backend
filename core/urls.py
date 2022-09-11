from django.urls import path
from .views import CurrencyListAPIView

urlpatterns = [
    path('currencies/', CurrencyListAPIView.as_view(), name="currencies")
]
