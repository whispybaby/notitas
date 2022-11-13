from django.shortcuts import render, redirect
from usuarios.forms import UsuariosFormulario, RestablecerFormulario
from django.urls import reverse

def registro(request):

    formulario = UsuariosFormulario()
    if request.method=='POST':
        print(request.POST)
        formulario = UsuariosFormulario(request.POST)
        if formulario.is_valid():
            print("es valido")
    return render(request, 'usuarios/registro.html', {
    'formulario' : formulario
    })

def recuperacion(request):
    formulario = RestablecerFormulario()
    return render(request, 'usuarios/recuperacion.html',{
    'recuperacion' : formulario
    })

