from django.db import models

# Create your models here.
class Reserva(models.Model):
    ID = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=20)
    fecha_reserva = models.DateField()
    fecha_reserva_hora = models.TimeField()
    cantidad_clientes = models.IntegerField()
    estado_reserva = models.CharField(max_length=20)
    observaciones = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cliente