# Generated by Django 4.1 on 2022-09-01 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_rename_funcionario_usuario_delete_cliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'managed': False},
        ),
    ]
