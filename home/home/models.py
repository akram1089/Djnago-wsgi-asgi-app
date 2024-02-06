# models.py

from django.utils import timezone

from django.db import models

class ExchangeData(models.Model):
    exchange = models.CharField(max_length=10)
    symbol = models.CharField(max_length=20)
    symbol_exp_data = models.JSONField()
    future_data = models.JSONField()
    data_option = models.JSONField()
    added_at = models.DateTimeField(default=timezone.now())  # Added field with default value


    def __str__(self):
        return f"{self.exchange} - {self.symbol}"


# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    secret_key = models.CharField(max_length=50, blank=True, null=True)
