# Generated by Django 4.0.3 on 2022-04-24 08:39

import LoginDetail.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginDetail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetail',
            name='imageUrl',
            field=models.ImageField(upload_to=LoginDetail.models.LoginDetail),
        ),
    ]