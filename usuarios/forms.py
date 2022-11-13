from django import forms
from .models import Usuarios
from django.forms import ModelForm, Form


class UsuariosFormulario(ModelForm):
    class Meta:
        model = Usuarios
        exclude = ['hash_contraseña']
        widgets = {
            'nombre': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'apellido': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'run':  forms.widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'pattern': '\d{1,2}\.\d{3}\.\d{3}-[\dk]'
                }
            ),

            'correo': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
    contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    confirmar_contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RestablecerFormulario(Form):
    correo = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    codigo_correo = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
