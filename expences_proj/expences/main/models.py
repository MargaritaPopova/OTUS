from django.contrib.auth.models import User
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Account(models.Model):

    sum = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Account of {self.user.first_name} {self.user.last_name}"


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    sum = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default=1)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction {self.id} at {self.created_at}'












