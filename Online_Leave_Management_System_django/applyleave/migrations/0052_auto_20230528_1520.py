# Generated by Django 2.2.4 on 2023-05-28 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0051_alter_leaveapplication_applied_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 28, 15, 20, 35, 274844), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 28, 15, 20, 35, 274844), null=True),
        ),
    ]
