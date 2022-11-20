from django.urls import path
from vehiculos import views as vehiculos
from mantenciones import views as mantenciones

app_name = 'vehiculos'
urlpatterns = [
    path('', vehiculos.index, name='index'),
    path('crear/', vehiculos.crear, name='crear'),
    path('<int:id>/', vehiculos.vehiculo, name='vehiculo'),
    path('<int:id>/actualizar', vehiculos.actualizar, name='actualizar'),
    path('<int:id>/eliminar', vehiculos.eliminar, name='eliminar'),
    path('<int:id_vehiculo>/mantenciones/registrar',
         mantenciones.registrar, name='crear_mantencion'),
    # path('<int:id_vehiculo>/mantenciones/<int:id_mantencion>/'),
    # path('<int:id_vehiculo>/mantenciones/<int:id_mantencion>/actualizar'),
    path('<int:id_vehiculo>/mantenciones/<int:id_mantencion>/eliminar' ,mantenciones.eliminar, name='eliminar_mantencion'),
]
