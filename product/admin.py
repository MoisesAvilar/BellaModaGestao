from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "note",
        "amount",
        "cost",
        "shipping",
        "value",
        "total",
        "profit",
    )
