# Generated by Django 5.1.2 on 2025-01-02 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0017_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
