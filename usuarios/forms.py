from django import forms
from .models import Usuario
from django.forms import ModelForm, Form
from notitas.helpers import validar_contraseña


class UsuariosFormulario(ModelForm):
    class Meta:
        model = Usuario
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

            'correo': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'nombre_usuario': forms.widgets.TextInput(
                attrs={
                    'maxlegth':'30', 
                    'minlegth':'5',
                    'class': 'form-control',

                }
            ),

        }
    contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_contraseña(self):
        contraseña = self.cleaned_data['contraseña']

        if contraseña and len(contraseña) < 8:
            raise forms.ValidationError('Ingrese al menos 8 carácteres')

        if not validar_contraseña(contraseña):
            raise forms.ValidationError(
                'Ingrese al menos una letra minúscula, mayúscula, un dígito y un símbolo')

        return contraseña


class RestablecerCuenta(Form):
    correo = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    codigo_correo = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}))

class IniciarSesion(Form):
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control',}))  
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control'}))

class EliminarSesion(Form):
    nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control',}))  
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control'}))

