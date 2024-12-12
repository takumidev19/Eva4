# Generated by Django 5.0.1 on 2024-12-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('telefono_cliente', models.CharField(max_length=20)),
                ('fecha_reserva', models.DateField()),
                ('fecha_reserva_hora', models.TimeField()),
                ('cantidad_clientes', models.IntegerField()),
                ('estado_reserva', models.CharField(max_length=20)),
                ('observaciones', models.CharField(max_length=100)),
            ],
        ),
    ]