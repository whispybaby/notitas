from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('registro', views.registro,  name='registro'),
]
