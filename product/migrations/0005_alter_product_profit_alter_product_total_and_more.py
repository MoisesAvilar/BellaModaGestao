# Generated by Django 5.1 on 2024-08-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_profit_product_total_product_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=8, null=True),
        ),
    ]
