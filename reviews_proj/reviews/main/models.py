from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):

    text = models.CharField(max_length=5000),
    grade = models.IntegerField(default=0),
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
