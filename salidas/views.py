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
from .models import Salida
from .forms import salidaForm
from producto.forms import stockForm
from django.core import urlresolvers
import datetime
from django.db.models import Q
def add_salida(request, producto_slug, template_name="add-salida.html"):
    p 				= get_object_or_404(Product, slug=producto_slug)
    salida 			= Salida.objects.all()
    page_title      = p.name
    #produccion_e 	= ProduccionEsperada.objects.filter(producto=p,fecha_a_agendar__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    if request.method == 'POST':
        form 			= salidaForm(request.POST)
        formproducto 	= stockForm(request.POST , instance=p)
        if form.is_valid() and formproducto.is_valid():
            salida     = form.save(commit = False)
            p = formproducto.save(commit = False)
            salida.save()
            p.save()
            return redirect(p.categoria.get_absolute_url())
    else:
        form    = salidaForm()
        formproducto = stockForm(request.POST , instance=p)
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'p':p,'salida':salida,}

    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def salidas(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    page_title  = "Salidas Realizadas"    
    template ="salidas.html"    
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_de_salida__icontains=query) 
        )
        results = Salida.objects.filter(qset)
        template_name = "search.html"
        return render_to_response(template_name, {"results": results,"query": query,'empleado':empleado},context_instance=RequestContext(request)) 
    else:
        results = []        
    salidas     = Salida.objects.filter(fecha_de_salida=datetime.datetime.today)
    args        = {'salidas':salidas,'page_title':page_title,'empleado':empleado}   
    return render_to_response(template, args,context_instance=RequestContext(request)) 

def salida(request, salida_id):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    salida = get_object_or_404(Salida, id=salida_id)
    page_title = salida.producto.name
    if request.method == 'POST':
        form = salidaForm(request.POST , instance=salida)
        formproducto    = stockForm(request.POST , instance=salida.producto)
        if form.is_valid() and formproducto.is_valid():
            salida     = form.save(commit = False)
            formproducto.save(commit = False)
            salida.save()
            formproducto.save()
            return redirect('salidas')
    else:
        form = salidaForm(request.POST , instance=salida)
        formproducto = stockForm(request.POST , instance=salida.producto)
    args = {}
    args.update(csrf(request))
    args ={'form':form,'salida':salida,}
    template_name="salida.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

"""
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_de_salida__icontains=query) 
        )
        results = Salida.objects.filter(qset)
    else:
        results = []

    template_name = "search.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 
"""