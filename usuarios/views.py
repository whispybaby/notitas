from django.shortcuts import render, redirect
from usuarios.forms import UsuariosFormulario
from django.urls import reverse

def listar(request):
    return render(request, 'libros/listar.html', {

    })
# Create your views here.
def registro(request):

    formulario = UsuariosFormulario()
    if request.method=='POST':
        formulario = UsuariosFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('usuarios:/listar'))
    return render(request, 'usuarios/registro.html', {
    'formulario' : formulario
    })
