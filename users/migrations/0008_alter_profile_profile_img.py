# Generated by Django 5.1.6 on 2025-03-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
