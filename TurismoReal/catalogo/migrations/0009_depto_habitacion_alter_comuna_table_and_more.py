# Generated by Django 4.1 on 2022-09-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_alter_comuna_options_alter_depto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='depto',
            name='habitacion',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterModelTable(
            name='comuna',
            table=None,
        ),
        migrations.AlterModelTable(
            name='depto',
            table=None,
        ),
        migrations.AlterModelTable(
            name='region',
            table=None,
        ),
        migrations.AlterModelTable(
            name='rol',
            table=None,
        ),
        migrations.AlterModelTable(
            name='usuario',
            table=None,
        ),
    ]
