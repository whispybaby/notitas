import datetime
from django import forms
from vehiculos.models import DetalleMantencion


class DetalleMantencionFormulario(forms.ModelForm):
    class Meta:
        fecha = datetime.datetime.now()
        año = fecha.year
        mes = fecha.month
        dia = fecha.day

        model = DetalleMantencion
        fields = '__all__'
        exclude = ('vehiculo',)
        widgets = {
            'mantencion': forms.widgets.Select(attrs={'class': 'form-select'}),
            'vehiculo': forms.widgets.Select(attrs={'class': 'form-select'}),
            'fecha': forms.widgets.DateInput(attrs={
                'class': 'form-control', 'type': 'date',
                'max': f'{año}-{mes}-{dia}',
                'min': f'{año - 1}-{mes}-1'
            }),
            'kilometraje': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }
