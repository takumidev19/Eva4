# Generated by Django 5.0.1 on 2024-12-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasApp', '0002_rename_fecha_reserva_hora_reserva_hora_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado_reserva',
            field=models.CharField(max_length=15),
        ),
    ]
