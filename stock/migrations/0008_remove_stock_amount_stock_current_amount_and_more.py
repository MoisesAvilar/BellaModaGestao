# Generated by Django 5.1 on 2024-09-03 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_quantity_sold'),
        ('stock', '0007_remove_stock_description_remove_stock_note_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='amount',
        ),
        migrations.AddField(
            model_name='stock',
            name='current_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='product.product'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='supplier',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
