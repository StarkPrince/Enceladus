# Generated by Django 3.1.6 on 2021-07-07 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210706_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 19, 47, 47, 431699)),
        ),
    ]
