from django.db import models
from mantenciones.models import Mantencion, DetalleMantencion


class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre


class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Tipo vehículo'
        verbose_name_plural = 'Tipos vehículos'

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return f'{self.marca.nombre} {self.nombre}'


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6)
    año = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    mantenciones = models.ManyToManyField(
        Mantencion, related_name='vehiculos', through=DetalleMantencion)

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f'{self.patente}: {self.marca.nombre} {self.modelo.nombre}'
