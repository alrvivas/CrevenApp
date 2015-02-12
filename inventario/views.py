from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext 
from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.core.context_processors import csrf

from producto.models import Product, Categoria
from devoluciones.models import DevolucionBuena,DevolucionMala,DevolucionReproceso
from salidas.models import Salida
from empleado.models import Empleado
from produccion.models import  ProduccionRealizada
#from .models import Inventario
#from .forms import inventarioForm
from producto.forms import stockForm
from django.core import urlresolvers
import datetime	
"""
def generar_inventario(request, template_name="generar-inventario.html"):
    page_title 		= "Generar Inventario"
    #inventario 		= Inventario.objects.all()
    entradas_pro 	= ProduccionRealizada.objects.filter(fecha_de_elaboracion__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    salidas 		= Salida.objects.filter(fecha_de_salida__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    devolucionr_r 	= DevolucionReproceso.objects.filter(fecha_de_entrada__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    devolucionr_b 	= DevolucionBuena.objects.filter(fecha_de_entrada__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    devolucionr_m 	= DevolucionMala.objects.filter(fecha_de_salida__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    if request.POST:
        form = inventarioForm(request.POST)
        if form.is_valid():
        	inventario = form.save(commit = False)
        	inventario.save()
        	return redirect('inventarios')
    else:
        form = inventarioForm()
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'p':p,'inventario':inventario,}
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def inventarios(request, template_name="inventarios.html"):
    page_title = "Inventarios"
    inventario  = Inventario.objects.all()    
    args ={'inventario':inventario,}

    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 
"""
def inventario(request):
    c           = Categoria.objects.all()
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    producto    = Product.objects.filter(categoria = c)
    salidas 	= Salida.objects.filter(producto=producto,fecha_de_salida__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    page_title  = "Inventario"
    template_name   = "inventario.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 
