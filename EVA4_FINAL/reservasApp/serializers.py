from rest_framework import serializers
from reservasApp.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
    
    def validate_cantidad_clientes(self, value):
        if value < 1 or value > 15:
            raise serializers.ValidationError("La cantidad de clientes debe estar entre 1 y 15.")
        return value

    def validate_estado_reserva(self, value):
        estados_validos = ['RESERVADO', 'COMPLETADA', 'ANULADA', 'NO_ASISTEN']
        if value not in estados_validos:
            raise serializers.ValidationError(f"El estado '{value}' no es válido. Los estados permitidos son: {', '.join(estados_validos)}.")
        return value