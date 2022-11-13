from django.db import models
from marcas.models import Marca
from tipos_vehiculos.models import TipoVehiculo


class Modelo(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return f'{self.marca.nombre} {self.nombre}'
