from django.shortcuts import render, redirect
from django.urls import reverse
from mantenciones.forms import DetalleMantencionFormulario
from vehiculos.models import DetalleMantencion, Vehiculo
from notitas.helpers import inicio_obligatorio


@inicio_obligatorio
def registrar(request, id_vehiculo):
    formulario = DetalleMantencionFormulario()
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    if request.method == 'POST':
        formulario = DetalleMantencionFormulario(request.POST)

        if formulario.is_valid():
            mantencion = formulario.save(commit=False)
            mantencion.vehiculo = vehiculo
            mantencion.save()
            return redirect(reverse('vehiculos:vehiculo', args=[id_vehiculo]))

        else:
            return render(request, 'mantenciones/crear.html', {
                'formulario': formulario,
                'operacion': 'Crear'
            })

    return render(request, 'mantenciones/crear.html', {
        'formulario': formulario,
        'operacion': 'Crear'
    })


@inicio_obligatorio
def eliminar(request, id_vehiculo, id_mantencion):
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    try:
        mantencion = DetalleMantencion.objects.get(
            id=id_mantencion, vehiculo=vehiculo)
    except DetalleMantencion.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    if request.method == 'POST':
        mantencion.delete()
        return redirect(reverse('vehiculos:vehiculo', args=[id_vehiculo]))

    return render(request, 'mantenciones/eliminar.html', {
        'mantencion': mantencion
    })


@inicio_obligatorio
def actualizar(request, id_vehiculo, id_mantencion):
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    try:
        mantencion = DetalleMantencion.objects.get(
            id=id_mantencion, vehiculo=vehiculo)
    except DetalleMantencion.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    formulario = DetalleMantencionFormulario(instance=mantencion)

    if request.method == 'POST':
        formulario = DetalleMantencionFormulario(
            request.POST, instance=mantencion)

        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('vehiculos:vehiculo', args=[id_vehiculo]))

        else:
            return render(request, 'mantenciones/crear.html', {
                'formulario': formulario,
                'operacion': 'Actualizar'
            })

    return render(request, 'mantenciones/crear.html', {
        'formulario': formulario,
        'operacion': 'Actualizar'
    })
