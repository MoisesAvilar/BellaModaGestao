# Generated by Django 5.1 on 2024-09-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_profit_alter_product_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_sold',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
