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
