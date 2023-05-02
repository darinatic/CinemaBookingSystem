# Generated by Django 4.2 on 2023-05-02 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_merge_0002_initial_0003_moviesession_start_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='cinemaroom',
            name='room_seat',
        ),
        migrations.RemoveField(
            model_name='foodandbeverage',
            name='combo_name',
        ),
        migrations.RemoveField(
            model_name='foodandbeverage',
            name='combo_price',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='purchased_date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_type',
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='session_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='start_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='combo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.foodandbeverage'),
        ),
    ]
