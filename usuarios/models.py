from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(unique=True)
    hash_contraseña = models.CharField(max_length=200)

    def clean(self) -> None:
        if len(self.nombre_usuario)<5:
            raise ValidationError('Formato invalido del nombre del usuario')  