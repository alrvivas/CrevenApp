#encoding:utf-8
from django import forms
from .models import *

class produccionForm(forms.ModelForm):

	class Meta:
		model = ProduccionEsperada

class produccionReForm(forms.ModelForm):

	class Meta:
		model = ProduccionRealizada