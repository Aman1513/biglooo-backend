# Generated by Django 4.0.3 on 2022-10-08 12:08

import Blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to=Blog.models.Blog),
        ),
    ]
