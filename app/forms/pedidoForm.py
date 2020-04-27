from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import *


from django.utils.safestring import mark_safe
class PictureWidget(forms.widgets.Widget):
	def render(self, name, value, attrs=None):
		html =  Template("""<img src="$link"/>""")
		return mark_safe(html.substitute(link=value))


from dal import autocomplete
class PedidoForm(ModelForm):
	class Meta:
		#imagen = models.ImageField(widget=PictureWidget)
		model = Pedido
		fields = {
			'tipopedido',
		}
		widgets = {
			'tipopedido': forms.TextInput(attrs={'type': 'number','class': 'form-control'}),
		}

	cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(estado=True), widget=autocomplete.ModelSelect2(url='cliente-autocomplete'))
	productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.filter(estado=True))
 

