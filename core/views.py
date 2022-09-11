from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Currency, Category
from .serializers import CurrencyListSerializer, CategorySerializer


# Create your views here.

class CurrencyListAPIView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
