# Generated by Django 4.2 on 2023-05-15 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_customer_alter_moviesession_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 18, 4, 14, 136593)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='purchased_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 18, 4, 14, 136593)),
        ),
    ]
