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
    currency = serializers.SlugRelatedField(slug_field='code',
                                            queryset=Currency.objects.all())  # Transaction has a Foreignkey with currency. when we submit a get request we just can see the id of currency. In this way we willl be able to see the code field of currency

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
