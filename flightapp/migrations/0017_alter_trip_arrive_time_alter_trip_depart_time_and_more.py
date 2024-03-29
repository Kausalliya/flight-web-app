# Generated by Django 4.1.7 on 2023-04-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0016_trip_arrival_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='arrive_time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='depart_time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='duration',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
