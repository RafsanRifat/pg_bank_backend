from django.urls import path, include
from rest_framework.authtoken import views
from .views import CurrencyListAPIView, CategoryViewSet, TransactionViewSet
from rest_framework import routers

router = routers.DefaultRouter()


router.register(r'category', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token),
    path('currencies/', CurrencyListAPIView.as_view(), name="currencies")
]
