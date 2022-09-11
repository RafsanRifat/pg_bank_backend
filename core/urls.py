from django.urls import path
from .views import CurrencyListAPIView, CategoryViewSet, TransactionViewSet
from rest_framework import routers

router = routers.SimpleRouter()


router.register(r'category', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('currencies/', CurrencyListAPIView.as_view(), name="currencies")
] + router.urls
