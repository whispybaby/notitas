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
            'año': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
        }
