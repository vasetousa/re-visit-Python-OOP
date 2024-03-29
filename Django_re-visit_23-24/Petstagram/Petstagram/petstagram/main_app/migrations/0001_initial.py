# Generated by Django 5.0.1 on 2024-02-05 17:17

import django.core.validators
import petstagram.main_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('type', models.IntegerField(choices=[(1, 'Dog'), (2, 'Cat'), (3, 'Fish'), (4, 'Parrot'), (5, 'Bunny'), (6, 'Other')])),
                ('date_of_birth', models.DateField()),
                ('photo', models.URLField()),
                ('description', models.TextField()),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.main_app.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.main_app.validators.validate_only_letters])),
                ('picture', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11, null=True)),
            ],
        ),
    ]
