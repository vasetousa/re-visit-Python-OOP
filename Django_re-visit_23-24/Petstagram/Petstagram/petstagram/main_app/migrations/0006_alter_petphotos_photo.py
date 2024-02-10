# Generated by Django 5.0.1 on 2024-02-05 19:00

import petstagram.main_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_petphotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphotos',
            name='photo',
            field=models.ImageField(upload_to='', validators=[petstagram.main_app.validators.validate_file_max_size_in_mb]),
        ),
    ]