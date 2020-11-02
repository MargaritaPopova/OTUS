from django.contrib.auth.models import User
from django.db import models


class TestModel(models.Model):

    name = models.CharField(max_length=64, default='')
    type = models.IntegerField(null=False)
    kind = models.CharField(max_length=64, default='')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Account(models.Model):

    sum = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Account of {self.user.get_username()}"


class Category(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    sum = models.IntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)












