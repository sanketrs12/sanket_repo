# Generated by Django 2.1 on 2018-11-23 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0013_auto_20181123_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 13, 57, 41, 366153), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]