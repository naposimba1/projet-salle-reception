# Generated by Django 4.1 on 2022-08-28 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sallere', '0015_remove_reservation_date_de_la_fete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date_reservation',
        ),
    ]