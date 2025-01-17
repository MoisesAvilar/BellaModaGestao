# Generated by Django 5.1 on 2024-09-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0006_alter_sale_total_alter_sale_unity_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sale',
            name='unity_value',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
        ),
    ]
