from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext 
from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.core.context_processors import csrf

from producto.models import Product
from empleado.models import Empleado
from .models import Saldo,Estatus
from .forms import saldoForm
from producto.forms import stockForm
from django.core import urlresolvers
import datetime	

def add_saldos(request, producto_slug, template_name="add-saldos.html"):
    p = get_object_or_404(Product, slug=producto_slug)
    page_title = p.name
    saldo 	= Saldo.objects.all()
    estatus = Estatus.objects.all()
    if request.method == 'POST':
        form            = saldoForm(request.POST)
        formproducto    = stockForm(request.POST , instance=p)
        if form.is_valid() and formproducto.is_valid():
            devolucion_b     = form.save(commit = False)
            p = formproducto.save(commit = False)
            devolucion_b.save()
            p.save()
            return redirect(p.get_absolute_url())
    else:
        form    = saldoForm()
        formproducto = stockForm(request.POST , instance=p)
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'formproducto':formproducto,'saldo':saldo,'p':p,'estatus':estatus,}
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def saldos(request, template_name="saldos.html"):
    page_title 		= "Saldos"
    saldos  	= Saldo.objects.all()    
    args 			= {'saldos':saldos,}
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def saldo(request, saldo_id):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    saldo = get_object_or_404(Saldo, id=saldo_id)
    page_title = saldo.producto.name
    if request.method == 'POST':
        form = saldoForm(request.POST , instance=saldo)
        if form.is_valid():
            saldo = form.save(commit = False)
            saldo.save()
            return redirect('saldos')
    else:
        form = saldoForm(request.POST , instance=saldo)
    args = {}
    args.update(csrf(request))
    args ={'form':form,'saldo':saldo}
    template_name="saldo.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  
