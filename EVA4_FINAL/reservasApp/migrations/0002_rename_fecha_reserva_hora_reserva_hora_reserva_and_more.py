# Generated by Django 5.0.1 on 2024-12-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='fecha_reserva_hora',
            new_name='hora_reserva',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado_reserva',
            field=models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], max_length=15),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='observaciones',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]