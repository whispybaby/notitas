from django.contrib import admin
from vehiculos.models import Modelo, Marca, TipoVehiculo

admin.site.register([Modelo, Marca, TipoVehiculo])
