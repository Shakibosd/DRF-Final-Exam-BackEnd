# Generated by Django 5.1.2 on 2024-12-31 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0006_plantrevivaltip_sunlight_needs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
