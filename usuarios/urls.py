from django.urls import path
from usuarios import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.registro, name='registro'),
    path('recuperacion/', views.recuperacion, name='recuperacion')
]
