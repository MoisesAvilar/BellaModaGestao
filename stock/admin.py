from django.contrib import admin
from stock.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'current_amount')
