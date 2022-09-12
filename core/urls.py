from django.urls import path, include
from .views import CurrencyListAPIView, CategoryViewSet, TransactionViewSet
from rest_framework import routers

router = routers.DefaultRouter()


router.register(r'category', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('currencies/', CurrencyListAPIView.as_view(), name="currencies")
]
