from django.urls import path
from vehiculos import views

app_name = 'vehiculos'
urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='crear'),
    path('<int:id>/', views.vehiculo, name='vehiculo'),
    path('<int:id>/actualizar', views.actualizar, name='actualizar'),
    path('<int:id>/eliminar', views.eliminar, name='eliminar'),
]
