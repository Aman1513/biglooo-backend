# Generated by Django 4.0.3 on 2022-03-25 09:12

import GovtJobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovtJobs', '0011_alter_govtjobs_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='govtjobs',
            name='logo',
            field=models.ImageField(upload_to=GovtJobs.models.GovtJobs),
        ),
    ]
