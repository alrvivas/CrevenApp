from django.conf.urls import patterns, include, url
from carro.views import CartDetails, CartItemDetail

urlpatterns = patterns('',
	url(r'^$', CartDetails.as_view(), name='cart'),
	url(r'^update/$', CartDetails.as_view(action='put'), name='cart_update'),
	
)