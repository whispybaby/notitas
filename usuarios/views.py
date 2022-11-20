from django.shortcuts import render, redirect
from usuarios.forms import UsuariosFormulario, RestablecerCuenta, IniciarSesion, EliminarSesion
from django.urls import reverse
from notitas.helpers import inicio_obligatorio, iniciar_sesion, cerrar_sesion, crear_hash, validar_hash
from usuarios.models import Usuario


def registro(request):
    formulario = UsuariosFormulario()

    if request.method == 'POST':
        formulario = UsuariosFormulario(request.POST)

        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.hash_contraseña = crear_hash(
                formulario.cleaned_data['contraseña'])
            usuario.save()

            iniciar_sesion(request, usuario)
            return redirect(reverse('vehiculos:index'))

    return render(request,  'usuarios/registro.html', {
        'formulario': formulario
    })


def iniciar(request):
    if request.method == 'POST':
        formulario = IniciarSesion(request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            contraseña = formulario.cleaned_data['contraseña']

            try:
                usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
            except Usuario.DoesNotExist:
                return render(request, 'usuarios/iniciar.html', {
                    'formulario': formulario,
                    'mensaje_error': 'usuario o contraseña incorrecta'
                })

            if validar_hash(usuario.hash_contraseña, contraseña):
                iniciar_sesion(request, usuario)
                return redirect(reverse('vehiculos:index'))

            else:
                return render(request, 'usuarios/iniciar.html', {
                    'formulario': formulario,
                    'mensaje_error': 'Usuario o contraseña incorrecta'
                })

    formulario = IniciarSesion()
    return render(request, 'usuarios/iniciar.html', {
        'formulario': formulario
    })


@inicio_obligatorio
def cerrar(request):
    cerrar_sesion(request)
    return redirect(reverse('usuarios:iniciar'))


@inicio_obligatorio
def eliminar(request):
    if request.method == 'POST':
        formulario = EliminarSesion(request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            contraseña = formulario.cleaned_data['contraseña']
            try:
                usuario = Usuario.objects.get(
                    id=request.session['id_usuario'], nombre_usuario=nombre_usuario)
            except Usuario.DoesNotExist:
                return redirect(reverse('usuarios:iniciar'))

            if validar_hash(usuario.hash_contraseña, contraseña):
                usuario.delete()
                cerrar_sesion(request)
                return redirect(reverse('usuarios:iniciar'))

    formulario = EliminarSesion()
    return render(request, 'usuarios/eliminar.html', {
        'formulario': formulario
    })
