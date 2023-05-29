# Generated by Django 2.1.5 on 2019-01-17 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0041_auto_20190117_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 15, 36, 38, 216061), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 17, 15, 36, 38, 217061), null=True),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='al_availed',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='al_closing_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='al_credited',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='al_opening_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='sdl_availed',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='sdl_closing_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='sdl_credited',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='leaveregister',
            name='sdl_opening_balance',
            field=models.FloatField(default=0),
        ),
    ]