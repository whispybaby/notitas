import hashlib
from functools import wraps
from django.shortcuts import redirect


def inicio_obligatorio(funcion, ruta_redireccion='usuarios:iniciar'):
    @wraps(funcion)
    def funcion_decorada(request, *args, **kwargs):
        if 'id_usuario' in request.session and not request.session['id_usuario'] is None:
            return funcion(request, *args, **kwargs)
        else:
            return redirect(ruta_redireccion)
    return funcion_decorada


def validar_contraseña(contraseña):
    puntuacion = 0
    mayusculas = 0
    minusculas = 0
    digitos = 0

    import string

    for caracter in contraseña:
        if caracter in string.ascii_lowercase:
            minusculas += 1

        if caracter in string.ascii_uppercase:
            mayusculas += 1

        if caracter in string.punctuation:
            puntuacion += 1

        if caracter in string.digits:
            digitos += 1

    if not puntuacion or not mayusculas or not minusculas or not digitos:
        return False

    return True


def iniciar_sesion(request, usuario):
    request.session['id_usuario'] = usuario.id
    request.session['nombre_usuario'] = usuario.nombre_usuario


def cerrar_sesion(request):
    request.session['id_usuario'] = None
    request.session['nombre_usuario'] = None


def crear_hash(contraseña):
    temporal = bytes(contraseña, encoding='utf-8')
    return hashlib.sha256(temporal).hexdigest()


def validar_hash(hash, contraseña):
    hash_temporal = crear_hash(contraseña)
    if hash == hash_temporal:
        return True
    else:
        return False
