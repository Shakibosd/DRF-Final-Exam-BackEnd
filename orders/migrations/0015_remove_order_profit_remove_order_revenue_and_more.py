# Generated by Django 5.1.6 on 2025-03-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_remove_order_transaction_id_order_profit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='order',
            name='revenue',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
