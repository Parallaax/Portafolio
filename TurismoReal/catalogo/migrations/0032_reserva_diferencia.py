# Generated by Django 4.1 on 2022-11-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0031_alter_depto_id_depto'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='diferencia',
            field=models.IntegerField(default=0),
        ),
    ]
