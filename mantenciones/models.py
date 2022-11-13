from django.db import models
from vehiculos.models import Vehiculo


class TipoMantencion(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Tipo mantención'
        verbose_name_plural = 'Tipos mantenciones'

    def __str__(self):
        return self.nombre


class Mantencion(models.Model):
    tipo_mantencion = models.ForeignKey(
        TipoMantencion, on_delete=models.RESTRICT)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT)
    precio = models.IntegerField()
    fecha = models.DateField()
    kilometraje = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Mantención'
        verbose_name_plural = 'Mantenciones'

    def __str__(self):
        return f'{self.tipo_mantencion.nombre} el {self.fecha}'
