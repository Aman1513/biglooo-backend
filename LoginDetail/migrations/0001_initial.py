# Generated by Django 4.0.3 on 2022-04-24 07:23

import LoginDetail.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('imageUrl', models.ImageField(upload_to=LoginDetail.models.LoginDetail)),
                ('givenName', models.CharField(max_length=50)),
                ('familyName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
                ('googleId', models.CharField(max_length=40)),
            ],
        ),
    ]
