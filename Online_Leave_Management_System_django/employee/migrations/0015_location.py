# Generated by Django 2.1 on 2018-11-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_auto_20181115_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]