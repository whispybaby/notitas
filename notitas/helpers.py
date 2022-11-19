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
