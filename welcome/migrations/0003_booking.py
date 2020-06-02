# Generated by Django 2.1.7 on 2019-04-01 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('welcome', '0002_auto_20190401_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('driver_name', models.CharField(max_length=30)),
                ('driver_license', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=10)),
                ('checkin_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('checkout_time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
            ],
        ),
    ]
