"""SistAlmacen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from app.Views.productoView import *
from app.Views.pedidoView import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', Login, name='Login'),
    path('home/', ProductoListar, name='Home'),
    path('', ProductoListar, name='home'),

    path('cliente-autocomplete/',ClienteAutocomplete.as_view(), name='cliente-autocomplete'),

    #path('producto/nuevo/', ProductoNuevo, name='Nuevo Producto'),
    
    path('pedido/', pedido_list, name='pedido_list'),
    path('pedido/listar/', pedido_list, name='pedido_list'),
    path('pedido/nuevo/',pedido_create,name='pedido_create'),

    ########################################################3
    #path('', views.ProductoList.as_view(), name='producto_list'),
    path('producto/', producto_list, name='producto_list'),
    path('producto/listar/', producto_list, name='producto_list'),
    path('producto/ver/<int:pk>', producto_view, name='producto_view'),
    path('producto/nuevo/', producto_create, name='producto_new'),
    path('producto/editar/<int:pk>', producto_update, name='producto_edit'),
    path('producto/eliminar/<int:pk>', producto_delete, name='producto_delete'),
    ##############################
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
