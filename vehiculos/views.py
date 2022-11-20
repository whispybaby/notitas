from django.shortcuts import render, redirect
from django.urls import reverse
from vehiculos.forms import VehiculoFormulario
from vehiculos.models import Vehiculo , DetalleMantencion
from notitas.helpers import inicio_obligatorio
from usuarios.models import Usuario

@inicio_obligatorio
def index(request):
    vehiculos = Vehiculo.objects.filter(usuario=request.session['id_usuario'])
    return render(request, 'vehiculos/index.html', {
        'vehiculos': vehiculos
    })

@inicio_obligatorio
def vehiculo(request, id):
    try:
        vehiculo = Vehiculo.objects.get(id=id)
        mantenciones = DetalleMantencion.objects.filter(vehiculo=vehiculo)
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:vehiculo'))
    return render(request, 'vehiculos/vehiculo.html', {
        'vehiculo': vehiculo,
        'mantenciones': mantenciones
    })

@inicio_obligatorio
def crear(request):
    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST)
        if formulario.is_valid():
            id_usuario = request.session['id_usuario'] 
            vehiculo = formulario.save(commit=False)
            vehiculo.usuario = Usuario.objects.get(id=id_usuario)
            vehiculo.save()
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

@inicio_obligatorio
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

@inicio_obligatorio
def eliminar(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect(reverse('vehiculos:index'))

    return render(request, 'vehiculos/eliminar.html', {
        'operacion': 'Eliminar',
        'vehiculo': vehiculo
    })
