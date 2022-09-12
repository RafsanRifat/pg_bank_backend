from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

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
    queryset = Transaction.objects.select_related('currency', 'category')
    # queryset = Transaction.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['amount', 'date']
    search_fields = ['amount', 'description', 'category__name']

    def get_serializer_class(self):
        if self.action in ("list", "retrive"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
