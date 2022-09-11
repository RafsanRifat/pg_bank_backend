from .models import Transaction
from rest_framework import serializers


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = True
        fields = ("id", "code", "name")