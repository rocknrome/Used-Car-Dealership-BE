# Generated by Django 5.0.3 on 2024-03-31 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, default='cars/default.jpeg', upload_to='cars'),
        ),
    ]
