#encoding:utf-8
from django import forms
from .models import *

class devolucionForm(forms.ModelForm):

	class Meta:
		model = DevolucionBuena

class devolucionMalaForm(forms.ModelForm):

	class Meta:
		model = DevolucionMala

class devolucionReprocesoForm(forms.ModelForm):

	class Meta:
		model = DevolucionReproceso