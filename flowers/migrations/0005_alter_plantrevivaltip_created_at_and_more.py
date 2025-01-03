# Generated by Django 5.1.2 on 2024-10-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0004_plantrevivaltip_delete_flowercaretip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='plant_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='recommended_fertilizer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='recommended_water_frequency',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='revival_steps',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='special_notes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='sunlight_adjustment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='symptoms',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='plantrevivaltip',
            name='watering_caution',
            field=models.CharField(max_length=100),
        ),
    ]
