from django.contrib import admin
from vehiculos.models import Modelo, Marca, TipoVehiculo, Mantencion

admin.site.register([Modelo, Marca, TipoVehiculo, Mantencion])
