from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    shipping = models.DecimalField(max_digits=6, decimal_places=2)
    note = models.TextField(max_length=255, blank=True, null=True)
    value = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, editable=False
    )
    total = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, editable=False
    )
    profit = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, editable=False
    )

    def clean(self):
        if self.amount < 0:
            raise ValidationError("The amount cannot be negative.")

        if self.cost < 0:
            raise ValidationError("The cost cannot be negative.")

        if self.shipping < 0:
            raise ValidationError("The shipping cannot be negative.")

    def save(self, *args, **kwargs):
        self.value = (self.amount * self.cost) + self.shipping
        self.total = (self.value / self.amount) * 2
        self.profit = self.total / 2
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description.title()
