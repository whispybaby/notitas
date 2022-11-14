from django.shortcuts import render, redirect
from django.urls import reverse
from vehiculos.forms import VehiculoFormulario


def index(request):
    return render(request, 'vehiculos/index.html')


def crear(request):
    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST)

        if formulario.is_valid():
            print(formulario.cleaned_data)
            return redirect(reverse('vehiculos:crear'))
        else:
            return render(request, 'vehiculos/crear.html', {
                'formulario': formulario
            })

    return render(request, 'vehiculos/crear.html', {
        'formulario': VehiculoFormulario()
    })
