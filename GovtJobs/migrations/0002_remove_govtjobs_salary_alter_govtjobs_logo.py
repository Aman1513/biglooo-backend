# Generated by Django 4.0.3 on 2022-03-22 04:43

import GovtJobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovtJobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='govtjobs',
            name='salary',
        ),
        migrations.AlterField(
            model_name='govtjobs',
            name='logo',
            field=models.ImageField(upload_to=GovtJobs.models.GovtJobs),
        ),
    ]
