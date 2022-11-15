import datetime
from django import forms
from vehiculos.models import Vehiculo


class VehiculoFormulario(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        exclude = ('mantenciones',)
        widgets = {
            'marca': forms.widgets.Select(attrs={'class': 'form-select'}),
            'modelo': forms.widgets.Select(attrs={'class': 'form-select'}),
            'año': forms.widgets.NumberInput(attrs={'class': 'form-control', 'min': '1970', 'max': f'{datetime.datetime.now().year}'}),
        }

    def clean_año(self):
        año = self.cleaned_data['año']
        if año > datetime.datetime.now().year or año < 1970:
            raise forms.ValidationError('Año incorrecto')
        return año

    def clean_modelo(self):
        modelo = self.cleaned_data['modelo']
        marca = self.cleaned_data['marca']
        if marca != modelo.marca:
            raise forms.ValidationError('El modelo no coincide con la marca')
        return modelo
