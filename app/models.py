from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    documento = models.CharField(max_length=8)
    direccion = models.CharField(max_length=45)
    estado = models.BooleanField(verbose_name=u"Estado",blank=True,default=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=45)
    estado = models.BooleanField(blank=True,default=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    nombre       = models.CharField(verbose_name=u"Nombre",max_length=45)
    categoria    = models.ForeignKey('Categoria',on_delete=models.CASCADE,verbose_name=u"Categoría",blank=True,null=True)
    #minicodigo   = models.CharField(verbose_name=u"Mini Código",max_length=45, blank=True, null=True)
    minicodigo   = models.CharField(verbose_name=u"Mini Código",max_length=45, blank=True, null=True)
    codigo_barra = models.CharField(verbose_name=u"Código de Barra",max_length=45, blank=True, null=True)
    cantidad     = models.FloatField(verbose_name=u"Cantidad",default=0,blank=True, null=True)
    imagen       = models.ImageField(verbose_name=u"Imagen",blank=True, null=True,default="producto-default.png")#upload_to='%Y/%m/%d',
    tipoproducto = models.IntegerField(verbose_name=u"Tipo Producto",default=1)
    estado       = models.BooleanField(verbose_name=u"Estado",blank=True,default=True)
    
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150"/>'.format(self.imagen.url))


    image_tag.short_description = 'Imagen'
    
class Pedido(models.Model):
    fechainicio    = models.DateTimeField(verbose_name=u"Fecha de Inicio",auto_now_add=True, blank=True)
    fechafin       = models.DateTimeField(verbose_name=u"Fecha de caducidad",auto_now_add=True, blank=True)    
    productos      = models.ManyToManyField(Producto)
    cliente        = models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)
    tipopedido     = models.IntegerField(blank = True, default=1)
    estado         = models.BooleanField(blank=True,default=True)

    class Meta:
        ordering = ["-fechainicio"]
    def __str__(self):
        cadena = str(self.fechainicio)+" - "+str(self.cliente)
        return cadena

class Pedidoproductos(models.Model):
    fecha        = models.DateTimeField(auto_now_add=True, blank=True)
    modificacion = models.DateTimeField(auto_now=True, blank=True)
    cantidad     = models.FloatField(default=0,blank=True, null=True)
    pedido       = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    producto     = models.ForeignKey(Producto,on_delete=models.CASCADE)
    activo       = models.BooleanField(blank=True,default=True)
    estado       = models.BooleanField(blank=True,default=True)

    class Meta:
        managed = False
        db_table = 'app_pedido_productos'

