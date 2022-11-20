from django.shortcuts import render, redirect
from django.urls import reverse
from mantenciones.forms import DetalleMantencionFormulario
from vehiculos.models import DetalleMantencion, Vehiculo
from notitas.helpers import inicio_obligatorio

@inicio_obligatorio
def registrar(request, id_vehiculo):
    formulario = DetalleMantencionFormulario()

    if request.method == 'POST':
        vehiculo = Vehiculo.objects.get(id=id_vehiculo)
        formulario = DetalleMantencionFormulario(request.POST)

        if formulario.is_valid():
            mantencion = formulario.save(commit=False)
            mantencion.vehiculo = vehiculo
            mantencion.save()
            return redirect(reverse('vehiculos:vehiculo', args=[id_vehiculo]))
        else:
            return render(request, 'mantenciones/crear.html', {
                'formulario': formulario
            })

    return render(request, 'mantenciones/crear.html', {
        'formulario': formulario
    })

@inicio_obligatorio
def eliminar(request, id_vehiculo, id_mantencion):
    mantencion = DetalleMantencion.objects.get(id=id_mantencion)
    if request.method == 'POST':
        mantencion.delete()
        return redirect(reverse('vehiculos:vehiculo', args=[id_vehiculo]))

    return render(request, 'mantenciones/eliminar.html', {
        'operacion': 'Eliminar',
        'matencion': mantencion
    })
