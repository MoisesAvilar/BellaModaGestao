from django.db import models
from product.models import Product


class Stock(models.Model):
    supplier = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0, editable=False)
    note = models.TextField(default="null", max_length=200, editable=False)

    def save(self, *args, **kwargs):
        self.amount = self.product.amount
        self.note = self.product.note

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Forncedor: {self.supplier} - Produto: {self.product} {self.note}"
