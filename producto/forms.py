#encoding:utf-8
from django import forms
from .models import Product

class stockForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['stock']


