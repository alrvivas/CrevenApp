from django.conf.urls import patterns, include, url
#from .views import ShopListView
#from .views import ProductDetailView
#from .models import Product

urlpatterns = patterns('',
	url(r'^$', 'empleado.views.index', name='index'), 
	url(r'^/login/$', 'empleado.views.LoginView', name='login'),
    url(r'^/logout/$', 'empleado.views.LogoutView', name='logout'),

)