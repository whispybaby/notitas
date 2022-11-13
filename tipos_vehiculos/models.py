from django.db import models


class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Tipo vehículo'
        verbose_name_plural = 'Tipos vehículos'

    def __str__(self):
        return self.nombre
