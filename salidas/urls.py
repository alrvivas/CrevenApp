from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^add-salida/(?P<producto_slug>[-\w]+)/$', 'salidas.views.add_salida',name='add_salida'),
	url(r'^$', 'salidas.views.salidas',name='salidas'),
	url(r'^salida/(?P<salida_id>[-\w]+)/$', 'salidas.views.salida',name='salida'),
	#url(r'^search/$', 'salidas.views.search'),	
) 