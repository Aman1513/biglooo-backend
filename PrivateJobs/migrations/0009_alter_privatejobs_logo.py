# Generated by Django 4.1.2 on 2022-10-22 19:08

import PrivateJobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrivateJobs', '0008_alter_privatejobs_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatejobs',
            name='logo',
            field=models.ImageField(upload_to=PrivateJobs.models.PrivateJobs),
        ),
    ]