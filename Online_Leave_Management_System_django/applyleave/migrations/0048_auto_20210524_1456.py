# Generated by Django 2.2.5 on 2021-05-24 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0047_auto_20210524_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 14, 56, 43, 339951), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 14, 56, 43, 342946), null=True),
        ),
    ]
