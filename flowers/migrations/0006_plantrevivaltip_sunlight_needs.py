# Generated by Django 5.1.2 on 2024-10-23 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0005_alter_plantrevivaltip_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantrevivaltip',
            name='sunlight_needs',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
