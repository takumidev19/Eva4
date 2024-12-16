"""
URL configuration for EVA4_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservasApp.views import ReservasList, ReservasDetail, index, agregarReserva, editarReserva, eliminarReserva, verReservas

urlpatterns = [
    path('', index, name='index'),
    path('verReservas/', verReservas, name='ver-reservas'),
    path('agregarReserva/', agregarReserva, name='agregar-reserva'),
    path('editarReserva/<int:pk>/', editarReserva, name='editar-reserva'),
    path('eliminarReserva/<int:pk>/', eliminarReserva, name='eliminar-reserva'),
    path('admin/', admin.site.urls, name='admin'),
    path('ReservasAPI/', ReservasList.as_view(), name='reservas-list'),
    path('ReservasAPI/<int:pk>/', ReservasDetail.as_view(), name='reservas-detail'),
]
