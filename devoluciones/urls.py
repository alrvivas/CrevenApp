from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^add-buena/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_buena',name='add_devolucion_buena'),
	url(r'^add-mala/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_mala',name='add_devolucion_mala'),
	url(r'^add-reproceso/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_reproceso',name='add_devolucion_reproceso'),
	url(r'^buenas/$', 'devoluciones.views.devoluciones_buenas',name='devoluciones_buenas'),
	url(r'^buena/(?P<devolucion_id>[-\w]+)/$', 'devoluciones.views.devolucion_buena',name='devolucion_buena'),
	url(r'^malas/$', 'devoluciones.views.devoluciones_malas',name='devoluciones_malas'),
	url(r'^mala/(?P<devolucion_id>[-\w]+)/$', 'devoluciones.views.devolucion_mala',name='devolucion_mala'),
	url(r'^reprocesos/$', 'devoluciones.views.devoluciones_reproceso',name='devoluciones_reproceso'),
	url(r'^reproceso/(?P<devolucion_id>[-\w]+)/$', 'devoluciones.views.devolucion_reproceso',name='devolucion_reproceso'),
	
	
) 