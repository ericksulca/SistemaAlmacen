from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import *


from django.utils.safestring import mark_safe
class PictureWidget(forms.widgets.Widget):
	def render(self, name, value, attrs=None):
		html =  Template("""<img src="$link"/>""")
		return mark_safe(html.substitute(link=value))

class ProductoForm(ModelForm):
	class Meta:
		#imagen = models.ImageField(widget=PictureWidget)
		model = Producto
		fields = ('nombre', 'imagen', 'categoria','minicodigo','codigo_barra','cantidad')
		widgets = {
			'nombre': forms.TextInput(attrs={'type': 'text','class': 'form-control', 'aria-describedby':'product name'}),
			'minicodigo': forms.TextInput(attrs={'type': 'text','class': 'form-control'}),
			'codigo_barra': forms.TextInput(attrs={'type': 'text','class': 'form-control'}),
			'cantidad': forms.TextInput(attrs={'type': 'number','class': 'form-control'}),
		}