from django.shortcuts import render, redirect
from django.urls import reverse
from vehiculos.forms import VehiculoFormulario, FiltrarVehiculosFormulario
from vehiculos.models import Vehiculo, DetalleMantencion
from notitas.helpers import inicio_obligatorio
from usuarios.models import Usuario


@inicio_obligatorio
def index(request):
    formulario = FiltrarVehiculosFormulario(request.GET)
    marca = request.GET.get('marca', None)
    año = request.GET.get('año', None)

    if marca and año:
        vehiculos = Vehiculo.objects.filter(usuario=request.session['id_usuario'], marca=marca, año=año)
    elif marca:
        vehiculos = Vehiculo.objects.filter(usuario=request.session['id_usuario'], marca=marca)
    elif año:
        vehiculos = Vehiculo.objects.filter(usuario=request.session['id_usuario'], año=año)
    else:
        vehiculos = Vehiculo.objects.filter(usuario=request.session['id_usuario'])

    return render(request, 'vehiculos/index.html', {
        'vehiculos': vehiculos,
        'formulario': formulario
    })


@inicio_obligatorio
def vehiculo(request, id_vehiculo):
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
        mantenciones = DetalleMantencion.objects.filter(vehiculo=vehiculo)
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))
    return render(request, 'vehiculos/vehiculo.html', {
        'vehiculo': vehiculo,
        'mantenciones': mantenciones
    })


@inicio_obligatorio
def crear(request):
    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST)

        if formulario.is_valid():
            vehiculo = formulario.save(commit=False)
            vehiculo.usuario = Usuario.objects.get(
                id=request.session['id_usuario'])
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
def actualizar(request, id_vehiculo):
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

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
def eliminar(request, id_vehiculo):
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    if request.method == 'POST':
        vehiculo.delete()
        return redirect(reverse('vehiculos:index'))

    return render(request, 'vehiculos/eliminar.html', {
        'vehiculo': vehiculo
    })
