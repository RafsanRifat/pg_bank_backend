from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Currency, Category, Transaction
from .serializers import CurrencyListSerializer, CategorySerializer, TransactionSerializer


# Create your views here.

class CurrencyListAPIView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
