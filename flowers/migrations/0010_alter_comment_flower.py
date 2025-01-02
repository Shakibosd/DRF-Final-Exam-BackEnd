# Generated by Django 5.1.2 on 2024-12-31 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0009_remove_comment_name_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='flower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='flowers.flower'),
        ),
    ]