from django.db import models
import uuid

# Create your models here.
opciones_moneda = [
    [0,"Dolares"],[1,"Pesos"]
]

class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='static/img/imgsubidas/', null=True, blank=True, verbose_name="image")
    nombre = models.CharField(max_length=80, verbose_name="nombre")
    telefono = models.CharField(max_length=12,null=True, blank=True,verbose_name="telefono")
    direccion = models.CharField(max_length=100,verbose_name="direccion",null=True, blank=True)
    correo = models.EmailField(verbose_name="correo")
    pais = models.CharField(max_length=30,verbose_name="pais")
    password = models.CharField(max_length=20,verbose_name="contrasenna")
    moneda = models.IntegerField(choices= opciones_moneda)

    def __str__(self):
        return self.nombre
