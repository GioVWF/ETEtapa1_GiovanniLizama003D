from django.urls import path
from .views import inicio, form_proveedor, Proveedores, form_mod_proveedor, form_del_proveedor
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name="inicio"),
    path('form-proveedor', form_proveedor, name="form_proveedor"),
    path('Proveedores', Proveedores, name="Proveedores"),
    path('form-mod-proveedor/<id>', form_mod_proveedor, name="form_mod_proveedor"),
    path('form-del-proveedor/<id>', form_del_proveedor, name="form_del_proveedor")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)