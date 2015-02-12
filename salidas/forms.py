#encoding:utf-8
from django import forms
from .models import *

class salidaForm(forms.ModelForm):

	class Meta:
		model = Salida
