from django.core.exceptions import ValidationError
from django.db import models
from product.models import Product
from stock.models import Stock
from django.db import transaction


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField(default=0)
    unity_value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, editable=False
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, editable=False
    )

    def clean(self):
        stock = Stock.objects.get(product=self.product)
        if self.quantity_sold > stock.current_amount:
            raise ValidationError("Quantity sold cannot exceed quantity in stock")

        if self.quantity_sold < 0:
            raise ValidationError("Quantity cannot be negative")

    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.unity_value = self.product.total
            self.total = self.unity_value * self.quantity_sold

            stock = Stock.objects.select_for_update().get(product=self.product)
            if self.quantity_sold > stock.current_amount:
                raise ValidationError("Not enough stock to complete the sale")

            stock.current_amount -= self.quantity_sold
            stock.save()

            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.description.title()} - {self.product.note.title()} - {self.quantity_sold}"
