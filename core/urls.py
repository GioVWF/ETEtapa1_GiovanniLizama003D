from django.urls import path
from .views import inicio, form_proveedor

urlpatterns = [
    path('inicio', inicio, name="inicio"),
    path('', form_proveedor, name="form_proveedor")
]