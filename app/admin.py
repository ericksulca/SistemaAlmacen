from django.contrib import admin
from app.models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('image_tag','nombre', 'codigo_barra', 'cantidad',)
    list_filter = ('categoria',)
    search_fields = ('nombre',)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Pedido)
