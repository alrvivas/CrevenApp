from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$','producto.views.catalogo', name='catalogo'),
	url(r'^categoria/(?P<categoria_slug>[-\w]+)/$','producto.views.ver_categoria', name='catalogo_categoria'), 
	url(r'^producto/(?P<producto_slug>[-\w]+)/$','producto.views.ver_producto',	name='product_detail'),
	url(r'^inventario/$', 'producto.views.inventario', name='inventario'),

  

)