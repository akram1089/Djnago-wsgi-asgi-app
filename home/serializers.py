# serializers.py
from rest_framework import serializers
from .models import ExchangeData

class ExchangeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeData
        fields = ['exchange', 'symbol', 'symbol_exp_data', 'future_data', 'data_option']
