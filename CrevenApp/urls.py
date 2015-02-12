from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CampoApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalogo/', include('producto.urls')),
    url(r'^carro/', include('carro.urls')),
    url(r'^checkout/', include('direccion.urls')),
    url(r'^salidas/', include('salidas.urls')),
    url(r'^produccion/', include('produccion.urls')),
    url(r'^devolucion/', include('devoluciones.urls')),
    url(r'^saldo/', include('saldo_anterior.urls')),
    url(r'^orden/',include('orden.urls')),
    url(r'^ship/',include('shipping.urls')),
    url(r'^pago/', include('payment.urls')),
    url(r'^$', 'empleado.views.index', name='index'), 
    url(r'^login/$', 'empleado.views.LoginView', name='login'),
    url(r'^logout/$', 'empleado.views.LogoutView', name='logout'),   
    
)
handler404 = 'productos.views.file_not_found_404' 
if settings.DEBUG == False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
   )