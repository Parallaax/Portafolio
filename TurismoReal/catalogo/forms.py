from faulthandler import disable
from django import forms
from django.forms import fields
from .models import *


class DeptoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    habitaciones = forms.IntegerField(min_value=1, max_value=8)
    precio = forms.IntegerField(min_value=100000, max_value=5000000)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Depto
        fields = '__all__'

class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

class TransporteForm(forms.ModelForm):

    class Meta:
        model = Transporte
        fields = '__all__'


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    estado = forms.CharField(widget=forms.TextInput(attrs={"id":"estado_in"}))
    class Meta:
        model = Reserva
        fields = ['estado']

class InventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = '__all__'