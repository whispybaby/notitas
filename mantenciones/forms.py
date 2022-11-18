from django import forms
from vehiculos.models import DetalleMantencion


class DetalleMantencionFormulario(forms.ModelForm):
    class Meta:
        model = DetalleMantencion
        fields = '__all__'
        exclude = ('vehiculo',)
        widgets = {
            'mantencion': forms.widgets.Select(attrs={'class': 'form-select'}),
            'vehiculo': forms.widgets.Select(attrs={'class': 'form-select'}),
            'precio': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'kilometraje': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }

    def clean_vehiculo(self):
        vehiculo = self.cleaned_data['vehiculo']
        print(vehiculo)
