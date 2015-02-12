#encoding:utf-8
from django import forms
from .models import *

class saldoForm(forms.ModelForm):

	class Meta:
		model = Saldo

