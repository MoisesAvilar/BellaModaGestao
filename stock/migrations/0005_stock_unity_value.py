# Generated by Django 5.1 on 2024-09-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_stock_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='unity_value',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
