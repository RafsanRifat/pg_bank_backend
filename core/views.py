from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Currency, Category, Transaction
from .serializers import CurrencyListSerializer, CategorySerializer, WriteTransactionSerializer, \
    ReadTransactionSerializer


# Create your views here.

class CurrencyListAPIView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrive"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
