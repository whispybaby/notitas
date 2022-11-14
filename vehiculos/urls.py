from django.urls import path
from vehiculos import views

app_name = 'vehiculos'
urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='crear'),
    path('<int:id>/', views.vehiculo, name='vehiculo'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]
