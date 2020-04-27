from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from SistAlmacen import settings
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from app.models import *
from app.forms.productoForm import *
import json
from myproject.myapp.models import UploadFileForm

class ProductoNuevo(CreateView):
    form_class = ProductoForm
    template_name = 'producto/nuevo.html'
    success_url = '/producto/listar'

@login_required
def ProductoListar(request):
    if request.method =='GET':
        oProductos =  Producto.objects.all().order_by('nombre')
        return render(request, "producto/listar.html", {'oProductos': oProductos})

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


def producto_list(request, template_name='producto/listar.html'):
    producto = Producto.objects.all()
    data = {}
    data['oProductos'] = producto
    return render(request, template_name, data)

def producto_view(request, pk, template_name='producto/nuevo.html'):
    producto= get_object_or_404(Producto, pk=pk)    
    return render(request, template_name, {'object':producto})

def producto_create(request, template_name='producto/nuevo.html'):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form = UploadForm(request.POST, request.FILES )
        print("File:"+ str(request.FILES))
        m = Producto.objects.get(pk=id)
        m.imagen = form.cleaned_data['imagen']
        m.save()
        return redirect('producto_list')
    return render(request, template_name, {'form':form})

def producto_update(request, pk, template_name='producto/producto_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('producto_list')
    return render(request, template_name, {'form':form})

def producto_delete(request, pk, template_name='producto/producto_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('producto_list')
    return render(request, template_name, {'object':book})