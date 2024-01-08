# models.py

from django.db import models

class ExchangeData(models.Model):
    exchange = models.CharField(max_length=10)
    symbol = models.CharField(max_length=20)
    symbol_exp_data = models.JSONField()
    future_data = models.JSONField()
    data_option = models.JSONField()

    def __str__(self):
        return f"{self.exchange} - {self.symbol}"
