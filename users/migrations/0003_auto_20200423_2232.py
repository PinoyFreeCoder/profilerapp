# Generated by Django 3.0.5 on 2020-04-23 14:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200423_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 14, 32, 23, 633606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 23, 14, 32, 23, 633606, tzinfo=utc)),
        ),
    ]
