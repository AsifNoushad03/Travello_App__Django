# Generated by Django 4.1.3 on 2022-12-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0009_booking_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
