# Generated by Django 4.0.3 on 2022-05-21 08:23

import PrivateJobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrivateJobs', '0005_alter_privatejobs_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatejobs',
            name='logo',
            field=models.ImageField(upload_to=PrivateJobs.models.PrivateJobs),
        ),
    ]