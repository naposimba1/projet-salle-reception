# Generated by Django 4.1 on 2022-08-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sallere', '0009_alter_reservation_a_payer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='a_payer',
            field=models.IntegerField(default=0),
        ),
    ]
