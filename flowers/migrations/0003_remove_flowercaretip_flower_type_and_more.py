# Generated by Django 5.1.2 on 2024-10-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_flowercaretip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowercaretip',
            name='flower_type',
        ),
        migrations.AlterField(
            model_name='flowercaretip',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
