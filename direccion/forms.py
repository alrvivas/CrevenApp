#-*- coding: utf-8 -*-
"""Forms for the django-shop app."""
from django import forms
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from backends_pool import backends_pool
from carro.models import CartItem
from .models import Address


def get_shipping_backends_choices():
    shipping_backends = backends_pool.get_shipping_backends_list()
    return tuple([(x.url_namespace, getattr(x, 'backend_verbose_name', x.backend_name)) for x in shipping_backends])


def get_billing_backends_choices():
    billing_backends = backends_pool.get_payment_backends_list()
    return tuple([(x.url_namespace, getattr(x, 'backend_verbose_name', x.backend_name)) for x in billing_backends])

class DireccionForm(forms.Form):

    class Meta:
        model = Address
 

class BillingShippingForm(forms.Form):
    """
    A form displaying all available payment and shipping methods (the ones
    defined in settings.SHOP_SHIPPING_BACKENDS and
    settings.SHOP_PAYMENT_BACKENDS)
    """
    shipping_method = forms.ChoiceField(choices=get_shipping_backends_choices(), label=('Shipping method'))
    payment_method = forms.ChoiceField(choices=get_billing_backends_choices(), label=('Payment method'))