# Generated by Django 4.0.3 on 2022-03-22 05:39

import GovtJobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovtJobs', '0002_remove_govtjobs_salary_alter_govtjobs_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='govtjobs',
            name='last_date',
            field=models.DateField(default='2022-03-23'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='govtjobs',
            name='logo',
            field=models.ImageField(upload_to=GovtJobs.models.GovtJobs),
        ),
    ]