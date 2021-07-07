from django.db import models
from django.forms.fields import IntegerField
import uuid

# Create your models here.
class Proveedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to='static/img/imgsubidas/', null=True, blank=True, verbose_name="image")
    nombre = models.CharField(max_length=80, verbose_name="nombre")
    telefono = models.IntegerField(null=True, blank=True,verbose_name="telefono")
    correo = models.EmailField(verbose_name="correo")
    pais = models.CharField(max_length=30,verbose_name="pais")
    password = models.CharField(max_length=20,verbose_name="contraseña")
    moneda = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="moneda")

    def __str__(self):
        return self.id
