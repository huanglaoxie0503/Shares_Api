# Generated by Django 3.0.7 on 2020-06-28 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='stockinfo',
            table='stock_info',
        ),
    ]