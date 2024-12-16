from django.db import models

# Create your models here.
class Reserva(models.Model):
    ESTADO_OPCIONES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    id = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=50)  # Nombre de quien realiza la reserva
    telefono_cliente = models.CharField(max_length=20)  # Teléfono de contacto
    fecha_reserva = models.DateField()  # Fecha de la reserva
    hora_reserva = models.TimeField()  # Hora de la reserva
    cantidad_clientes = models.IntegerField()  # Cantidad de personas
    estado_reserva = models.CharField(max_length=15, choices=ESTADO_OPCIONES)  # Estado de la reserva
    observaciones = models.CharField(max_length=100, blank=True, null=True)  # Observaciones (no requerido)

    def __str__(self):
        return f"Reserva {self.id} - {self.nombre_cliente} ({self.estado_reserva})"
