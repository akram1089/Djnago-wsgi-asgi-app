# admin.py

from django.contrib import admin
from .models import ExchangeData

@admin.register(ExchangeData)
class ExchangeDataAdmin(admin.ModelAdmin):
    list_display = ('exchange', 'symbol',)
    search_fields = ('exchange', 'symbol',)
    # Add other configurations as needed


# admin.py
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
