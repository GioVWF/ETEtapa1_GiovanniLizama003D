from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    image = forms.ImageField(label='imagen',
    widget=forms.ClearableFileInput(
        attrs={
            'class':'form-control'
        }
    ))
    nombre = forms.CharField(label="nombre completo", max_length=80, widget=forms.TextInput(
        attrs={
            'class':'forms-control'
        }
    ))
    telefono = forms.IntegerField(label='telefono', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    correo = forms.EmailField(label="correo electrónico", widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    pais = forms.CharField(label="país", max_length=30, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    password = forms.CharField(label="contraseña", max_length=20,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    moneda = forms.DecimalField(label="dolares", widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Proveedor
        fields = ('image','nombre','telefono','correo','pais','password','moneda')
