from django.db import models
from product.models import Product


class Stock(models.Model):
    supplier = models.CharField(max_length=100)
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    current_amount = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.current_amount = self.product.amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Product: {self.product.description.title()} - Current stock: {self.current_amount}"
