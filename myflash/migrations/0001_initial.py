# Generated by Django 3.1.5 on 2021-01-28 19:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlashCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('images', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
            ],
        ),
    ]
<<<<<<< HEAD
=======

>>>>>>> e7881adcbd8b41ac64f14c989b13c8aea580c599
