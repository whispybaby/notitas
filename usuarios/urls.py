from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.registro, name='registro'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('cerrar/', views.cerrar, name='cerrar'),
    path('eliminar/', views.eliminar, name='eliminar'),
]
