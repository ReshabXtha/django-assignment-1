# Generated by Django 3.0.5 on 2020-07-18 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLG', '0004_auto_20200718_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 18, 17, 22, 43, 209437)),
        ),
    ]
