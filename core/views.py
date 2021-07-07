from django.shortcuts import redirect, render
from .forms import ProveedorForm
from .models import Proveedor
# Create your views here.

def inicio(request):
    proveedores=Proveedor.objects.all()
    datos = {
        'proveedores':proveedores
    }
    return render(request, 'core/inicio.html', datos)

def Proveedores(request):
    proveedores=Proveedor.objects.all()
    datos = {
        'proveedores':proveedores
    }
    return render(request, 'core/Proveedores.html', datos)

def form_mod_proveedor(request,id):
    proveedores=Proveedor.objects.get(id=id)
    datos = {
        'form':ProveedorForm(instance=proveedores)
    }
    return render(request, 'core/form_proveedor_mod.html', datos)

def form_del_proveedor(request,id):
    proveedores=Proveedor.objects.get(id=id)
    proveedores.delete()
    return redirect(to="inicio")

def form_proveedor(request):
    data = {
        'form':ProveedorForm()
    }
    if request.method== "POST":
        form = ProveedorForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()   
        print (form.errors)
    return render(request, 'core/form_proveedor.html', data)
       
      