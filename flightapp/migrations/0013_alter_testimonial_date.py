# Generated by Django 4.1.7 on 2023-04-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0012_alter_testimonial_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]