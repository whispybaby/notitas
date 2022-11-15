from django.shortcuts import render, redirect
from usuarios.forms import UsuariosFormulario, RestablecerCuenta, IniciarSesion , EliminarSesion
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
import hashlib
from usuarios.models import Usuarios



def crear_hash(contraseña):
    temporal = bytes(contraseña, encoding='utf-8')
    return hashlib.sha256(temporal).hexdigest()


def validar_hash(hash, contraseña):
    hash_temporal = crear_hash(contraseña)
    if hash == hash_temporal:
        return True
    else:
        return False



def registro(request):

    formulario = UsuariosFormulario()
    if request.method == 'POST':
        formulario = UsuariosFormulario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.hash_contraseña = crear_hash(
                formulario.cleaned_data['contraseña'])
            usuario.save()
            return redirect (reverse('usuarios:iniciar'))

    return render(request, 'usuarios/registro.html', {
        'formulario': formulario
    })


def recuperacion(request):
    formulario = RestablecerCuenta()
    return render(request, 'usuarios/recuperacion.html', {
        'recuperacion': formulario
    })


def iniciar(request):
    if request.method == "POST":
        formulario = IniciarSesion(request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get("nombre_usuario")
            contraseña = formulario.cleaned_data.get("contraseña")
            # obtener usuario con correo

            try:
                usuario = Usuarios.objects.get(nombre_usuario=nombre_usuario)
                
            except Usuarios.DoesNotExist:
                return render(request,'usuarios/iniciar.html',{
                    'formulario': formulario,
                    'mensaje_error': 'usuario o contraseña incorrecta' 
                })
            
            contraseñacifrada = usuario.hash_contraseña

            if validar_hash(contraseñacifrada, contraseña):
                request.session['id_usuario'] = usuario.nombre_usuario
                print (request.session['id_usuario'])
                return redirect (reverse ('usuarios:registro'))
                
            
            else:
                return render(request,'usuarios/iniciar.html',{
                    'formulario': formulario,
                    'mensaje_error': 'usuario o contraseña incorrecta' 
                })
    formulario = IniciarSesion()
    return render(request, 'usuarios/iniciar.html', {
    'formulario': formulario
    })

def cerrar(request):
    print ('cerrando sesion')
    request.session['id_usuario'] = None
    return redirect(reverse('usuarios:iniciar'))
    
def eliminar(request):
    if request.method == "POST":
        formulario = EliminarSesion(request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get("nombre_usuario")
            contraseña = formulario.cleaned_data.get("contraseña")
            usuario = Usuarios.objects.filter(nombre_usuario=nombre_usuario).first()
            print(usuario)


            contraseñacifrada = usuario.hash_contraseña
            
            if validar_hash(contraseñacifrada, contraseña):
                request.session['id_usuario'] = usuario.nombre_usuario
                print (request.session['id_usuario'])
                usuario.delete()
                request.session['id_usuario'] = None
                return redirect(reverse('usuarios:iniciar'))

    formulario = EliminarSesion()
    return render(request, 'usuarios/eliminar.html', {
        'formulario': formulario
    })           
