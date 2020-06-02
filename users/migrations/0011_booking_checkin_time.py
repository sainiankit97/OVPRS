# Generated by Django 2.1.7 on 2019-04-01 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_booking_checkin_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='checkin_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
