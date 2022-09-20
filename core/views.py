from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from .models import Currency, Category, Transaction
from .serializers import CurrencyListSerializer, CategorySerializer, WriteTransactionSerializer, \
    ReadTransactionSerializer


# Create your views here.

class CurrencyListAPIView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    # queryset = Transaction.objects.all()
    # queryset = Transaction.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['amount', 'date']
    search_fields = ['amount', 'description', 'category__name']

    def get_queryset(self):
        return Transaction.objects.select_related('currency', 'category', 'user').filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrive"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
