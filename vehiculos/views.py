from django.shortcuts import render
from vehiculos.forms import VehiculoFormulario


def index(request):
    return render(request, 'vehiculos/index.html')


def crear(request):
    return render(request, 'vehiculos/crear.html', {
        'formulario': VehiculoFormulario()
    })
