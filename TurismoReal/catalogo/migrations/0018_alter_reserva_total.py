# Generated by Django 4.1 on 2022-10-22 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0017_alter_reserva_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
