from django.forms import ModelForm, widgets
from .models import Usuarios


class UsuariosFormulario(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'apellido': widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'run':  widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'correo': widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'hash_contraseña': widgets.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'valor_max': widgets.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
