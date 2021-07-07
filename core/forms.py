from django import forms
from .models import Proveedor
from django.db.models import fields
from django.forms import ModelForm, widgets, ImageField, FileField

class ProveedorForm(forms.ModelForm):
    id = forms.CharField(label='Número de identificación', widget=forms.TextInput( attrs={
        'class':'forms-control',
        'placeholder':'Ingrese identificación',
        'autofocus':'autofocus'
    }
    ))
    image = forms.ImageField(label='Imagen',
            widget=forms.ClearableFileInput(
            attrs={
                'class':'forms-control',
                'name':'image' 
            }
            ))
    nombre = forms.CharField(label="Nombre", max_length=80, widget=forms.TextInput(
        attrs={
            'class':'forms-control',
            'placeholder':'Ingrese nombre completo'
        }
    ))
    telefono = forms.CharField(max_length=12,label='Telefóno', widget=forms.TextInput(
        attrs={
            'class':'forms-control',
            'placeholder':'Ingrese telefóno'
        }
    ))
    direccion = forms.CharField(max_length=100,label="Dirección",widget=forms.TextInput(
        attrs={
            'class':'forms-control',
            'placeholder':'Ingrese Dirección'
        }
    ))
    correo = forms.EmailField(label="Correo Electrónico", widget=forms.EmailInput(
        attrs={
            'class':'forms-control',
            'placeholder':'Ingrese correo electrónico'
        }
    ))
    pais = forms.CharField(label="país", max_length=30, widget=forms.TextInput(
        attrs={
            'class':'forms-control',
            'placeholder':'Ingrese país'
        }
    ))
    password = forms.CharField(label="Contraseña", max_length=20,widget=forms.TextInput(
        attrs={
            'class':'forms-control',
            'placeholder':'Ingrese contraseña'
        }
    ))
    class Meta:
        model = Proveedor
        fields = ['id','image','nombre','telefono','correo','pais','password','moneda']
    