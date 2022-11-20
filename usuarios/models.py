from django.db import models
from django.core.exceptions import ValidationError


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(unique=True)
    hash_contraseña = models.CharField(max_length=200)
