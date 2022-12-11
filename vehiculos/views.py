from django.shortcuts import render, redirect
from django.urls import reverse
from vehiculos.forms import VehiculoFormulario, FiltrarMantencionesFormulario
from vehiculos.models import Vehiculo, DetalleMantencion
from notitas.helpers import inicio_obligatorio
from usuarios.models import Usuario
from datetime import datetime
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import xlwt
import json
from reportlab.pdfgen import canvas


@inicio_obligatorio
def index(request):
    vehiculos = Vehiculo.objects.filter(usuario=request.session['id_usuario'])
    return render(request, 'vehiculos/index.html', {
        'vehiculos': vehiculos
    })


@inicio_obligatorio
def vehiculo(request, id_vehiculo):
    formulario = FiltrarMantencionesFormulario(request.GET)
    mantencion = request.GET.get('mantencion', None)
    inicio_fecha = request.GET.get('fecha_inicial', "1970-01-01")
    final_fecha = request.GET.get(
        'fecha_final', datetime.today().strftime("%Y-%m-%d"))
    if inicio_fecha == "":
        inicio_fecha = "1970-01-01"
    if final_fecha == "":
        final_fecha = datetime.today().strftime("%Y-%m-%d")
    inicio = datetime.strptime(inicio_fecha, "%Y-%m-%d").date()
    final = datetime.strptime(final_fecha, "%Y-%m-%d").date()

    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])

        if mantencion:
            mantenciones = DetalleMantencion.objects.filter(
                vehiculo=vehiculo, mantencion=mantencion, fecha__gte=inicio, fecha__lte=final)
        else:
            mantenciones = DetalleMantencion.objects.filter(
                vehiculo=vehiculo, fecha__gte=inicio, fecha__lte=final)
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))
    return render(request, 'vehiculos/vehiculo.html', {
        'vehiculo': vehiculo,
        'mantenciones': mantenciones,
        'formulario': formulario,

    })


@inicio_obligatorio
def exportar_mantenciones(request, id_vehiculo):
    tipo = request.GET.get('formato', None)
    mantencion = request.GET.get('mantencion', None)
    inicio_fecha = request.GET.get('fecha_inicial', "1970-01-01")
    final_fecha = request.GET.get(
        'fecha_final', datetime.today().strftime("%Y-%m-%d"))
    if inicio_fecha == "":
        inicio_fecha = "1970-01-01"
    if final_fecha == "":
        final_fecha = datetime.today().strftime("%Y-%m-%d")
    inicio = datetime.strptime(inicio_fecha, "%Y-%m-%d").date()
    final = datetime.strptime(final_fecha, "%Y-%m-%d").date()
    print(tipo)
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])

        if mantencion:
            mantenciones = DetalleMantencion.objects.filter(
                vehiculo=vehiculo, mantencion=mantencion, fecha__gte=inicio, fecha__lte=final)
        else:
            mantenciones = DetalleMantencion.objects.filter(
                vehiculo=vehiculo, fecha__gte=inicio, fecha__lte=final)

        if tipo == 'excel':
            respuesta = HttpResponse(content_type='application/ms-excel')
            respuesta['Content-Disposition'] = 'attachment; filename="mantenciones.xls"'
            archivouwu = xlwt.Workbook(encoding='utf-8')
            hoja = archivouwu.add_sheet('Mantenciones')

            hoja.write(0, 0, 'tipo mantencion')
            hoja.write(0, 1, 'fecha')
            hoja.write(0, 2, 'kilometraje')
            hoja.write(0, 3, 'descripcion')

            fila = 1
            for mantencion in mantenciones:
                hoja.write(fila, 0, str(mantencion.mantencion))
                hoja.write(fila, 1, str(mantencion.fecha))
                hoja.write(fila, 2, mantencion.kilometraje)
                hoja.write(fila, 3, mantencion.descripcion)
                fila += 1

            archivouwu.save(respuesta)

        elif tipo == 'xml':
            respuesta = HttpResponse(content_type='application/xml')
            respuesta['Content-Disposition'] = 'attachment; filename="mantenciones.xml"'
            raiz = ET.Element('mantenciones')
            for mantencion in mantenciones:
                tipo_mantencion = ET.SubElement(raiz, 'tipo_mantencion')
                tipo_mantencion.text = str(mantencion.mantencion)
                fecha = ET.SubElement(raiz, 'fecha')
                fecha.text = str(mantencion.fecha)
                kilometraje = ET.SubElement(raiz, 'kilometraje')
                kilometraje.text = str(mantencion.kilometraje)
                descripcion = ET.SubElement(raiz, 'descripcion')
                descripcion.text = str(mantencion.descripcion)
            respuesta.write(ET.tostring(raiz))
        elif tipo == 'pdf':
            respuesta = HttpResponse(content_type='application/pdf')
            respuesta['Content-Disposition'] = 'attachment; filename="mantenciones.pdf"'
            pdf = canvas.Canvas(respuesta)
            pdf.drawString(100, 800, 'mantenciones')
            pdf.drawString(100, 780, 'tipo mantencion')
            pdf.drawString(200, 780, 'fecha')
            pdf.drawString(300, 780, 'kilometraje')
            pdf.drawString(400, 780, 'descripcion')
            fila = 760
            for mantencion in mantenciones:
                pdf.drawString(100, fila, str(mantencion.mantencion))
                pdf.drawString(200, fila, str(mantencion.fecha))
                pdf.drawString(300, fila, str(mantencion.kilometraje))
                pdf.drawString(400, fila, str(mantencion.descripcion))
                fila -= 20
            pdf.showPage()
            pdf.save()
        elif tipo == 'json':
            respuesta = HttpResponse(content_type='application/json')
            respuesta['Content-Disposition'] = 'attachment; filename="mantenciones.json"'
            matenciones_json = []
            for mantencion in mantenciones:
                matenciones_json.append({
                    'tipo_mantencion': str(mantencion.mantencion),
                    'fecha': str(mantencion.fecha),
                    'kilometraje': str(mantencion.kilometraje),
                    'descripcion': str(mantencion.descripcion)
                })
            respuesta.write(json.dumps(matenciones_json))

    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    return respuesta


@inicio_obligatorio
def crear(request):
    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST)

        if formulario.is_valid():
            vehiculo = formulario.save(commit=False)
            vehiculo.usuario = Usuario.objects.get(
                id=request.session['id_usuario'])
            vehiculo.save()
            return redirect(reverse('vehiculos:index'))

        else:
            return render(request, 'vehiculos/crear.html', {
                'formulario': formulario,
                'operacion': 'Crear'
            })

    return render(request, 'vehiculos/crear.html', {
        'formulario': VehiculoFormulario(),
        'operacion': 'Crear'
    })


@inicio_obligatorio
def actualizar(request, id_vehiculo):
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    if request.method == 'POST':
        formulario = VehiculoFormulario(request.POST, instance=vehiculo)

        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('vehiculos:index'))
        else:
            return render(request, 'vehiculos/crear.html', {
                'formulario': formulario,
                'operacion': 'Actualizar'
            })

    return render(request, 'vehiculos/crear.html', {
        'formulario': VehiculoFormulario(instance=vehiculo),
        'operacion': 'Actualizar'
    })


@inicio_obligatorio
def eliminar(request, id_vehiculo):
    try:
        vehiculo = Vehiculo.objects.get(
            id=id_vehiculo, usuario=request.session['id_usuario'])
    except Vehiculo.DoesNotExist:
        return redirect(reverse('vehiculos:index'))

    if request.method == 'POST':
        vehiculo.delete()
        return redirect(reverse('vehiculos:index'))

    return render(request, 'vehiculos/eliminar.html', {
        'vehiculo': vehiculo
    })
