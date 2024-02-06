# admin.py

from django.contrib import admin
from .models import ExchangeData

@admin.register(ExchangeData)
class ExchangeDataAdmin(admin.ModelAdmin):
    list_display = ('exchange', 'symbol',)
    search_fields = ('exchange', 'symbol',)
    # Add other configurations as needed
# Import the correct CustomUser model
from .models import CustomUser

# Register the CustomUser model if it's not registered already
admin.site.register(CustomUser)
