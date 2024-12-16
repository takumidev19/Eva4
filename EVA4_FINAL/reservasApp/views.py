from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reserva
from .serializers import ReservaSerializer
from rest_framework.exceptions import NotFound
import requests
from .forms import ReservaForm

def index(request):
    return render(request, 'index.html')

def verReservas(request):
    api_url = 'http://127.0.0.1:8000/ReservasAPI/'
    response = requests.get(api_url)
    data = response.json() if response.status_code == 200 else []
    return render(request, 'Reservas/verReservas.html', {'data': data})

def agregarReserva(request):
    if request.method == 'POST':
        api_url = "http://127.0.0.1:8000/ReservasAPI/"
        payload = {
            "nombre_cliente": request.POST.get("nombre_cliente"),
            "telefono_cliente": request.POST.get("telefono_cliente"),
            "fecha_reserva": request.POST.get("fecha_reserva"),
            "hora_reserva": request.POST.get("hora_reserva"),
            "cantidad_clientes": request.POST.get("cantidad_clientes"),
            "estado_reserva": request.POST.get("estado_reserva"),
            "observaciones": request.POST.get("observaciones"),
        }
        response = requests.post(api_url, json=payload)

        if response.status_code in [200, 201]:
            return redirect('index')  # Redirigir al index después de agregar la reserva
        else:
            # Obtener los errores de la API y mostrarlos como mensajes de error
            errores = response.json()
            if 'cantidad_clientes' in errores:
                for error in errores['cantidad_clientes']:
                    messages.error(request, error)

            return render(request, 'Reservas/agregarReservas.html')

    return render(request, 'Reservas/agregarReservas.html')

def editarReserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'Reservas/editarReserva.html', {'form': form, 'reserva': reserva})

def eliminarReserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('index')  # Redirige a la página principal después de eliminar
    return render(request, 'Reservas/eliminarReservas.html', {'reserva': reserva})

class ReservasList(APIView):
    def get(self, request):
        # Listar todas las reservas ordenadas por fecha
        reservas = Reserva.objects.all().order_by('fecha_reserva', 'hora_reserva')
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Crear una nueva reserva
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservasDetail(APIView):
    def get_object(self, pk):
        try:
            return Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            raise NotFound(detail="No se encontró la reserva.")  # Manejo estándar de excepciones

    def get(self, request, pk):
        # Obtener una reserva por ID
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    def put(self, request, pk):
        # Actualizar una reserva existente
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Eliminar una reserva existente
        reserva = self.get_object(pk)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
