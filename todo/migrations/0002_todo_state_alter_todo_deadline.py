# Generated by Django 4.2.4 on 2024-02-19 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='state',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 19, 17, 58, 0, 844788)),
        ),
    ]
