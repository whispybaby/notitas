from django.db import models
import re
from django.core.exceptions import ValidationError
# Create your models here.


class Usuarios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    run = models.CharField(primary_key=True, unique=True, max_length=12)
    correo = models.EmailField()
    hash_contraseña = models.CharField(max_length=200)

    def clean(self) -> None:
        if not re.search('\d{1,2}\.\d{3}\.\d{3}-[\dk]', self.run):
            raise ValidationError('Formato invalido del run')  