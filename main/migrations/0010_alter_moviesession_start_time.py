# Generated by Django 4.2 on 2023-05-02 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_moviesession_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 23, 31, 4, 360271)),
        ),
    ]