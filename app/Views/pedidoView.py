from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from SistAlmacen import settings
from django.contrib.auth.decorators import login_required

from app.models import *
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from app.forms.pedidoForm import *


def pedido_list(request, template_name='pedido/listar.html'):
    pedido = Pedido.objects.all()
    data = {}
    data['oPedidos'] = pedido
    return render(request, template_name, data)

def pedido_view(request, pk, template_name='pedido/nuevo.html'):
    pedido= get_object_or_404(Pedido, pk=pk)    
    return render(request, template_name, {'object':pedido})

def pedido_create(request, template_name='pedido/nuevo.html'):
    form = PedidoForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect('pedido_list')
    return render(request, template_name, {'form':form})

def pedido_update(request, pk, template_name='pedido/pedido_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('pedido_list')
    return render(request, template_name, {'form':form})

def pedido_delete(request, pk, template_name='pedido/pedido_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('pedido_list')
    return render(request, template_name, {'object':book})