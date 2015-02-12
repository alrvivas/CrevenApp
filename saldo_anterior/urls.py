from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^add-saldo/(?P<producto_slug>[-\w]+)/$', 'saldo_anterior.views.add_saldos',name='add_saldo'),
	url(r'^saldos/$', 'saldo_anterior.views.saldos',name='saldos'),
	url(r'^saldo/(?P<saldo_id>[-\w]+)$', 'saldo_anterior.views.saldo',name='saldo'),
)