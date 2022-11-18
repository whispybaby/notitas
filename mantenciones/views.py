from django.shortcuts import render
from mantenciones.forms import DetalleMantencionFormulario
from vehiculos.models import Vehiculo


def registrar(request, id_vehiculo):
    formulario = DetalleMantencionFormulario()

    if request.method == 'POST':
        vehiculo = Vehiculo.objects.get(id=id_vehiculo)
        formulario = DetalleMantencionFormulario(request.POST)

        if formulario.is_valid():
            print(formulario.cleaned_data)
        
        else:
            print(request.POST)

    return render(request, 'mantenciones/crear.html', {
        'formulario': formulario
    })
