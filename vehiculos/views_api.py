from rest_framework.decorators import api_view
from rest_framework.response import Response
from vehiculos.models import Vehiculo
from vehiculos.serializers import VehiculoSerializer
from django.shortcuts import render


@api_view(['GET' , 'POST'])
def  vehiculos(request):
    if request.method == 'GET':
        try: 
            marca = int(request.GET.get('marca'))
        except:
            marca = None
        if marca:
            vehiculos = Vehiculo.objects.filter(marca=marca)
        else:
            vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vehiculo(request, id):
    try:
        vehiculo = Vehiculo.objects.get(pk=id)
    except Vehiculo.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehiculoSerializer(vehiculo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vehiculo.delete()
        return Response(status=204)
