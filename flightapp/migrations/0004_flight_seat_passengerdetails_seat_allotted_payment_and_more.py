# Generated by Django 4.1.7 on 2023-03-27 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flightapp', '0003_experiences_alter_hotel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='flight_seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A1', models.BooleanField(default=True)),
                ('B1', models.BooleanField(default=True)),
                ('C1', models.BooleanField(default=True)),
                ('D1', models.BooleanField(default=True)),
                ('E1', models.BooleanField(default=True)),
                ('F1', models.BooleanField(default=True)),
                ('A2', models.BooleanField(default=True)),
                ('B2', models.BooleanField(default=True)),
                ('C2', models.BooleanField(default=True)),
                ('D2', models.BooleanField(default=True)),
                ('E2', models.BooleanField(default=True)),
                ('F2', models.BooleanField(default=True)),
                ('A3', models.BooleanField(default=True)),
                ('D3', models.BooleanField(default=True)),
                ('E3', models.BooleanField(default=True)),
                ('F3', models.BooleanField(default=True)),
                ('A4', models.BooleanField(default=True)),
                ('B4', models.BooleanField(default=True)),
                ('C4', models.BooleanField(default=True)),
                ('D4', models.BooleanField(default=True)),
                ('E4', models.BooleanField(default=True)),
                ('F4', models.BooleanField(default=True)),
                ('A5', models.BooleanField(default=True)),
                ('B5', models.BooleanField(default=True)),
                ('C5', models.BooleanField(default=True)),
                ('D5', models.BooleanField(default=True)),
                ('E5', models.BooleanField(default=True)),
                ('F5', models.BooleanField(default=True)),
                ('A6', models.BooleanField(default=True)),
                ('B6', models.BooleanField(default=True)),
                ('C6', models.BooleanField(default=True)),
                ('D6', models.BooleanField(default=True)),
                ('E6', models.BooleanField(default=True)),
                ('F6', models.BooleanField(default=True)),
                ('A7', models.BooleanField(default=True)),
                ('B7', models.BooleanField(default=True)),
                ('C7', models.BooleanField(default=True)),
                ('D7', models.BooleanField(default=True)),
                ('E7', models.BooleanField(default=True)),
                ('F7', models.BooleanField(default=True)),
                ('A8', models.BooleanField(default=True)),
                ('B8', models.BooleanField(default=True)),
                ('C8', models.BooleanField(default=True)),
                ('D8', models.BooleanField(default=True)),
                ('E8', models.BooleanField(default=True)),
                ('F8', models.BooleanField(default=True)),
                ('A9', models.BooleanField(default=True)),
                ('B9', models.BooleanField(default=True)),
                ('C9', models.BooleanField(default=True)),
                ('D9', models.BooleanField(default=True)),
                ('E9', models.BooleanField(default=True)),
                ('F9', models.BooleanField(default=True)),
                ('A10', models.BooleanField(default=True)),
                ('B10', models.BooleanField(default=True)),
                ('C10', models.BooleanField(default=True)),
                ('D10', models.BooleanField(default=True)),
                ('E10', models.BooleanField(default=True)),
                ('F10', models.BooleanField(default=True)),
                ('A11', models.BooleanField(default=True)),
                ('B11', models.BooleanField(default=True)),
                ('C11', models.BooleanField(default=True)),
                ('D11', models.BooleanField(default=True)),
                ('E11', models.BooleanField(default=True)),
                ('F11', models.BooleanField(default=True)),
                ('A12', models.BooleanField(default=True)),
                ('B12', models.BooleanField(default=True)),
                ('C12', models.BooleanField(default=True)),
                ('D12', models.BooleanField(default=True)),
                ('E12', models.BooleanField(default=True)),
                ('F12', models.BooleanField(default=True)),
                ('A13', models.BooleanField(default=True)),
                ('B13', models.BooleanField(default=True)),
                ('C13', models.BooleanField(default=True)),
                ('D13', models.BooleanField(default=True)),
                ('E13', models.BooleanField(default=True)),
                ('F13', models.BooleanField(default=True)),
                ('A14', models.BooleanField(default=True)),
                ('B14', models.BooleanField(default=True)),
                ('C14', models.BooleanField(default=True)),
                ('D14', models.BooleanField(default=True)),
                ('E14', models.BooleanField(default=True)),
                ('F14', models.BooleanField(default=True)),
                ('A15', models.BooleanField(default=True)),
                ('B15', models.BooleanField(default=True)),
                ('C15', models.BooleanField(default=True)),
                ('D15', models.BooleanField(default=True)),
                ('E15', models.BooleanField(default=True)),
                ('F15', models.BooleanField(default=True)),
                ('A16', models.BooleanField(default=True)),
                ('B16', models.BooleanField(default=True)),
                ('C16', models.BooleanField(default=True)),
                ('D16', models.BooleanField(default=True)),
                ('E16', models.BooleanField(default=True)),
                ('F16', models.BooleanField(default=True)),
                ('A17', models.BooleanField(default=True)),
                ('B17', models.BooleanField(default=True)),
                ('C17', models.BooleanField(default=True)),
                ('D17', models.BooleanField(default=True)),
                ('E17', models.BooleanField(default=True)),
                ('F17', models.BooleanField(default=True)),
                ('A18', models.BooleanField(default=True)),
                ('B18', models.BooleanField(default=True)),
                ('C18', models.BooleanField(default=True)),
                ('D18', models.BooleanField(default=True)),
                ('E18', models.BooleanField(default=True)),
                ('F18', models.BooleanField(default=True)),
                ('A19', models.BooleanField(default=True)),
                ('B19', models.BooleanField(default=True)),
                ('C19', models.BooleanField(default=True)),
                ('D19', models.BooleanField(default=True)),
                ('E19', models.BooleanField(default=True)),
                ('F19', models.BooleanField(default=True)),
                ('A20', models.BooleanField(default=True)),
                ('B20', models.BooleanField(default=True)),
                ('C20', models.BooleanField(default=True)),
                ('D20', models.BooleanField(default=True)),
                ('E20', models.BooleanField(default=True)),
                ('F20', models.BooleanField(default=True)),
                ('A21', models.BooleanField(default=True)),
                ('B21', models.BooleanField(default=True)),
                ('C21', models.BooleanField(default=True)),
                ('D21', models.BooleanField(default=True)),
                ('E21', models.BooleanField(default=True)),
                ('F21', models.BooleanField(default=True)),
                ('A22', models.BooleanField(default=True)),
                ('B22', models.BooleanField(default=True)),
                ('C22', models.BooleanField(default=True)),
                ('D22', models.BooleanField(default=True)),
                ('E22', models.BooleanField(default=True)),
                ('F22', models.BooleanField(default=True)),
                ('A23', models.BooleanField(default=True)),
                ('B3', models.BooleanField(default=True)),
                ('C3', models.BooleanField(default=True)),
                ('D23', models.BooleanField(default=True)),
                ('E23', models.BooleanField(default=True)),
                ('F23', models.BooleanField(default=True)),
                ('A24', models.BooleanField(default=True)),
                ('B24', models.BooleanField(default=True)),
                ('C24', models.BooleanField(default=True)),
                ('D24', models.BooleanField(default=True)),
                ('E24', models.BooleanField(default=True)),
                ('F24', models.BooleanField(default=True)),
                ('A25', models.BooleanField(default=True)),
                ('B25', models.BooleanField(default=True)),
                ('C25', models.BooleanField(default=True)),
                ('D25', models.BooleanField(default=True)),
                ('E25', models.BooleanField(default=True)),
                ('F25', models.BooleanField(default=True)),
                ('A26', models.BooleanField(default=True)),
                ('B26', models.BooleanField(default=True)),
                ('C26', models.BooleanField(default=True)),
                ('D26', models.BooleanField(default=True)),
                ('E26', models.BooleanField(default=True)),
                ('F26', models.BooleanField(default=True)),
                ('A27', models.BooleanField(default=True)),
                ('B27', models.BooleanField(default=True)),
                ('C27', models.BooleanField(default=True)),
                ('D27', models.BooleanField(default=True)),
                ('E27', models.BooleanField(default=True)),
                ('F27', models.BooleanField(default=True)),
                ('A28', models.BooleanField(default=True)),
                ('B28', models.BooleanField(default=True)),
                ('C28', models.BooleanField(default=True)),
                ('D28', models.BooleanField(default=True)),
                ('E28', models.BooleanField(default=True)),
                ('F28', models.BooleanField(default=True)),
                ('A29', models.BooleanField(default=True)),
                ('B29', models.BooleanField(default=True)),
                ('C29', models.BooleanField(default=True)),
                ('D29', models.BooleanField(default=True)),
                ('E29', models.BooleanField(default=True)),
                ('F29', models.BooleanField(default=True)),
                ('A30', models.BooleanField(default=True)),
                ('B30', models.BooleanField(default=True)),
                ('C30', models.BooleanField(default=True)),
                ('D30', models.BooleanField(default=True)),
                ('E30', models.BooleanField(default=True)),
                ('F30', models.BooleanField(default=True)),
                ('A31', models.BooleanField(default=True)),
                ('B31', models.BooleanField(default=True)),
                ('C31', models.BooleanField(default=True)),
                ('D31', models.BooleanField(default=True)),
                ('E31', models.BooleanField(default=True)),
                ('F31', models.BooleanField(default=True)),
                ('A32', models.BooleanField(default=True)),
                ('B32', models.BooleanField(default=True)),
                ('C32', models.BooleanField(default=True)),
                ('D32', models.BooleanField(default=True)),
                ('E32', models.BooleanField(default=True)),
                ('F32', models.BooleanField(default=True)),
                ('A33', models.BooleanField(default=True)),
                ('B33', models.BooleanField(default=True)),
                ('C33', models.BooleanField(default=True)),
                ('D33', models.BooleanField(default=True)),
                ('E33', models.BooleanField(default=True)),
                ('F33', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='passengerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(max_length=30)),
                ('sufix', models.CharField(blank=True, max_length=30, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mob', models.CharField(blank=True, max_length=30, null=True)),
                ('redness_num', models.IntegerField(blank=True, null=True)),
                ('traveller_num', models.IntegerField(blank=True, null=True)),
                ('checkedbag', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='seat_allotted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatnumber', models.CharField(max_length=30)),
                ('passengerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightapp.passengerdetails')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cardnumber', models.CharField(max_length=30)),
                ('expirationdate', models.CharField(max_length=100)),
                ('ccv', models.CharField(max_length=30)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emergency_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('mob', models.CharField(max_length=30)),
                ('passengerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightapp.passengerdetails')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
