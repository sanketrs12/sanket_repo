# Generated by Django 2.2.5 on 2021-05-24 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0048_auto_20210524_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 15, 4, 23, 47121), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 15, 4, 23, 49119), null=True),
        ),
    ]
