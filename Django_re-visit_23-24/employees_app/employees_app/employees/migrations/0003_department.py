# Generated by Django 4.0.2 on 2024-02-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]