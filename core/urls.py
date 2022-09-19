from django.urls import path, include
from rest_framework.authtoken import views
from .views import CurrencyListAPIView, CategoryViewSet, TransactionViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_framework.urls')),
    path('login/', views.obtain_auth_token),
    path('currencies/', CurrencyListAPIView.as_view(), name="currencies")
    # path('currencies/', CurrencyListAPIView.as_view(), name="currencies")
]
