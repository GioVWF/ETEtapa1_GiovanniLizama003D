from django.shortcuts import render
from .forms import ProveedorForm
# Create your views here.

def inicio(request):
    return render(request, 'core/inicio.html')

def form_proveedor(request):
    data={
        'form':ProveedorForm()
    }
    if request.method=='POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
    return render(request, 'core/form_proveedor.html',data)
  
          
      