# Generated by Django 4.2 on 2023-05-05 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_moviesession_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 5, 17, 56, 55, 833640)),
        ),
    ]
