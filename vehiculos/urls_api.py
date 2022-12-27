from django.urls import path
from vehiculos import views_api
urlpatterns = [
    path('', views_api.vehiculos, name='vehiculos'),
    path('<int:id>/', views_api.vehiculo, name='vehiculo'),
]