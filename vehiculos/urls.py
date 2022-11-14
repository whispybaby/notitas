from django.urls import path
from vehiculos import views

app_name = 'vehiculos'
urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='crear'),
]
