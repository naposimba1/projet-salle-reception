# Generated by Django 2.2.28 on 2022-11-15 10:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='nom_client',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='phone_client',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='prenom_client',
            new_name='prenom',
        ),
        migrations.RenameField(
            model_name='type_decor',
            old_name='code_decor',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='type_decor',
            old_name='montant_decor',
            new_name='montant',
        ),
        migrations.RenameField(
            model_name='type_decor',
            old_name='nom_decor',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='type_fete',
            old_name='code_fete',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='type_fete',
            old_name='montant_fete',
            new_name='montant',
        ),
        migrations.RenameField(
            model_name='type_fete',
            old_name='nom_fete',
            new_name='nom',
        ),
        migrations.AddField(
            model_name='reservation',
            name='date_de_reservation',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='a_payer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_payer_total',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='type_decor',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, to='api.Type_Decor'),
            preserve_default=False,
        ),
    ]
