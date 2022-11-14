from django.shortcuts import render, redirect
from django.urls import reverse
from vehiculos.forms import VehiculoFormulario
from vehiculos.models import Vehiculo


def index(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/index.html', {
        'vehiculos': vehiculos
    })


def vehiculo(request, id):
    try:
        vehiculo = Vehiculo.objects.get(id=id)
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))
    return render(request, 'vehiculos/vehiculo.html', {
        'vehiculo': vehiculo
    })


def crear(request):
    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('vehiculos:index'))
        else:
            return render(request, 'vehiculos/crear.html', {
                'formulario': formulario,
                'operacion': 'Crear'
            })

    return render(request, 'vehiculos/crear.html', {
        'formulario': VehiculoFormulario(),
        'operacion': 'Crear'
    })


def actualizar(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST, instance=vehiculo)

        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('vehiculos:index'))
        else:
            return render(request, 'vehiculos/crear.html', {
                'formulario': formulario,
                'operacion': 'Actualizar'
            })

    return render(request, 'vehiculos/crear.html', {
        'formulario': VehiculoFormulario(instance=vehiculo),
        'operacion': 'Actualizar'
    })


def eliminar(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect(reverse('vehiculos:index'))

    return render(request, 'vehiculos/eliminar.html', {
        'operacion': 'Eliminar',
        'vehiculo': vehiculo
    })
