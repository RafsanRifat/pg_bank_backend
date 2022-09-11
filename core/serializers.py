from .models import Transaction, Currency, Category
from rest_framework import serializers


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category",
        )
