# Generated by Django 4.1 on 2022-09-01 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comuna',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='depto',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='rol',
            options={'managed': False},
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='catalogo_usuario',
        ),
    ]