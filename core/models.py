from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.code


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name="transactions")
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="transactions")

    def __str__(self):
        return f"{self.amount} {self.currency} {self.date}"
