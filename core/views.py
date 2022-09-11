from django.shortcuts import render
from rest_framework import generics

from .models import Currency
from .serializers import CurrencyListSerializer


# Create your views here.

class CurrencyListAPIView(generics.ListAPIView):
    serializer_class = CurrencyListSerializer
    queryset = Currency.objects.all()
