# Generated by Django 5.0.3 on 2024-03-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]