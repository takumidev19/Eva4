from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        
    def clean_cantidad_clientes(self):
        value = self.cleaned_data['cantidad_clientes']
        if value < 1 or value > 15:
            raise forms.ValidationError("La cantidad de clientes debe estar entre 1 y 15.")
        return value

    def clean_estado_reserva(self):
        estados_validos = ['RESERVADO', 'COMPLETADA', 'ANULADA', 'NO_ASISTEN']
        value = self.cleaned_data['estado_reserva']
        if value not in estados_validos:
            raise forms.ValidationError(f"El estado '{value}' no es válido. Los estados permitidos son: {', '.join(estados_validos)}.")
        return value

    def clean_observaciones(self):
        # Si 'observaciones' está vacío o solo tiene espacios, devolver 'none'
        value = self.cleaned_data['observaciones']
        if value is None or not value.strip():
            return 'none'
        return value    