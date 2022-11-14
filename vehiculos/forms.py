from django import forms
from vehiculos.models import Vehiculo


class VehiculoFormulario(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        exclude = ('mantenciones',)
        widgets = {
            'patente': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'año': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'marca': forms.widgets.Select(attrs={'class': 'form-select'}),
            'modelo': forms.widgets.Select(attrs={'class': 'form-select'})
        }
