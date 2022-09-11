from django.urls import path
from .views import CurrencyListAPIView, CategoryViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('currencies/', CurrencyListAPIView.as_view(), name="currencies")
] + router.urls
