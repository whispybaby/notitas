from django.db import models


class TipoMantencion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo mantención'
        verbose_name_plural = 'Tipos mantenciones'

    def __str__(self):
        return self.nombre
