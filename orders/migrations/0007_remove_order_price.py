# Generated by Django 5.1.2 on 2024-10-28 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
    ]
