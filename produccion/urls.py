from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^capturar-esperada/(?P<producto_slug>[-\w]+)/$', 'produccion.views.produccion_esperada',{'template_name':'produccion-esperada.html'},name='produccion_esperada'),
	url(r'^realizada/(?P<producto_slug>[-\w]+)/$', 'produccion.views.produccion_realizada',{'template_name':'produccion-realizada.html'},name='produccion_realizada'),
	url(r'^esperadas/$', 'produccion.views.producciones_esperadas',name='producciones_esperadas'),
	url(r'^ver-esperada/(?P<produccione_id>[-\w]+)/$', 'produccion.views.esperada',name='esperada'),
	url(r'^realizadas/$', 'produccion.views.producciones_realizadas',name='producciones_realizadas'),
	url(r'^ver-realizada/(?P<produccionr_id>[-\w]+)/$', 'produccion.views.realizada',name='realizada'),
	
) 