# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext 
from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.core.context_processors import csrf
from django.core import urlresolvers
from django.core.urlresolvers import reverse

from .forms import stockForm
from .models import Product
from categoria.models import Categoria
from empleado.models import Empleado
from devoluciones.models import DevolucionBuena,DevolucionMala,DevolucionReproceso
from salidas.models import Salida
from saldo_anterior.models import Saldo
from produccion.models import  ProduccionRealizada
from django.views.generic import TemplateView, ListView, DetailView, View
import datetime 


class ProductDetailView(DetailView):
    
    model = Product  # It must be the biggest ancestor of the inheritence tree.
    generic_template = 'producto.html'

    def get_template_names(self):
        ret = super(ProductDetailView, self).get_template_names()
        if not self.generic_template in ret:
            ret.append(self.generic_template)
        return ret

"""class ShopListView(ListView):"""

@login_required(login_url='/login/')
def catalogo(request):
    page_title 	= "Catalogo"
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    #empleado    = Empleado.objects.all()
    producto 	= Product.objects.all()     
    categorias 	= Categoria.objects.all() 
    args 		= {'page_title':page_title,'producto':producto,'categorias':categorias,'empleado':empleado}
    return render_to_response('catalogo.html', args, context_instance=RequestContext(request))

def ver_categoria(request, categoria_slug):
    c = get_object_or_404(Categoria, slug=categoria_slug)
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    producto = c.product_set.all()
    page_title = c.nombre
    template_name = "categoria.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def ver_producto(request, producto_slug):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    p = get_object_or_404(Product, slug=producto_slug)
    page_title = p.name
    if request.method == 'POST':
        form = stockForm(request.POST , instance=p)
        if form.is_valid():
            p = form.save(commit = False)
            p.save()
            return redirect(p.get_absolute_url())
    else:
        form = stockForm(request.POST , instance=p)
        args = {}
        args.update(csrf(request))
        args ={'form':form,'p':p}
    template_name="producto.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  

def inventario(request):
    c           = Categoria.objects.all()
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    producto    = Product.objects.filter(categoria = c)
    salidas     = Salida.objects.filter(producto=producto,fecha_de_salida=datetime.datetime.today())
    entradas_p  = ProduccionRealizada.objects.filter(producto=producto,fecha_de_elaboracion=datetime.datetime.today())
    devolucion_r  = DevolucionReproceso.objects.filter(producto=producto,fecha_de_entrada=datetime.datetime.today())
    devolucion_b  = DevolucionBuena.objects.filter(producto=producto,fecha_de_entrada=datetime.datetime.today())
    devolucion_m  = DevolucionMala.objects.filter(producto=producto,fecha_de_salida=datetime.datetime.today())
    saldo       = Saldo.objects.filter(producto=producto,fecha_cracion=datetime.datetime.today()- datetime.timedelta(days=1))
   
    page_title  = "Inventario"
    template_name   = "inventario.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  



def file_not_found_404(request):
    page_title = 'ups esto no esta bien'
    return render_to_response('404.html', locals(), context_instance=RequestContext(request)) 
