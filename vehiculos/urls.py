from django.urls import path
from vehiculos import views as vehiculos
from mantenciones import views as mantenciones

app_name = 'vehiculos'
urlpatterns = [
    path('', vehiculos.index, name='index'),
    path('exportar_vehiculos', vehiculos.exportar_vehiculos, name='exportar_vehiculos'),
    path('crear/', vehiculos.crear, name='crear'),
    path('<int:id_vehiculo>/', vehiculos.vehiculo, name='vehiculo'),
    path('<int:id_vehiculo>/actualizar',
         vehiculos.actualizar, name='actualizar'),
    path('<int:id_vehiculo>/eliminar', vehiculos.eliminar, name='eliminar'),
    path('<int:id_vehiculo>/mantenciones/registrar',
         mantenciones.registrar, name='crear_mantencion'),
    path('<int:id_vehiculo>/mantenciones/<int:id_mantencion>/actualizar',
         mantenciones.actualizar, name='actualizar_mantencion'),
    path('<int:id_vehiculo>/mantenciones/<int:id_mantencion>/eliminar',
         mantenciones.eliminar, name='eliminar_mantencion'),
    path('<int:id_vehiculo>/exportar_mantenciones/',
         vehiculos.exportar_mantenciones, name='exportar_mantenciones'),
]
