from django.contrib.auth.models import User

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


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class WriteTransactionSerializer(serializers.ModelSerializer):
    # currency = serializers.SlugRelatedField(slug_field='code',
    #                                         queryset=Currency.objects.all())  # Transaction has a Foreignkey with currency. when we submit a get request we just can see the id of currency. In this way we willl be able to see the code field of currency
    # category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault())  # user set korar jonno viewset a amra j perform_create method likhechi, seita na likhe ekhan theke evabeo serializer set kore dewa jabe
    #     default=serializers.CurrentUserDefault())  # user set korar jonno viewset a amra j perform_create method likhechi, seita na likhe ekhan theke evabeo serializer set kore dewa jabe

    class Meta:
        model = Transaction
        fields = (
            # "user",   serializer theke user set kore dite chaile eikhane user field define korte hobe
            "amount",
            "currency",
            "date",
            "description",
            "category",
        )


class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencyListSerializer()
    category = CategorySerializer()
    user = ReadUserSerializer()

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "currency",
            "date",
            "description",
            "category",
            'user'
        )
