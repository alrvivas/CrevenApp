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
from devoluciones.models import DevolucionReproceso
from .models import ProduccionEsperada, ProduccionRealizada
from .forms import produccionForm, produccionReForm
from producto.forms import stockForm
from django.core import urlresolvers
import datetime	
from django.db.models import Q

def produccion_esperada(request, producto_slug, template_name="produccion-esperada.html"):
    p = get_object_or_404(Product, slug=producto_slug)
    page_title = p.name
    produccion 	= ProduccionEsperada.objects.all()  
    if request.POST:
        form = produccionForm(request.POST)
        if form.is_valid():
        	produccion = form.save(commit = False)
        	produccion.save()
        	return redirect(p.get_absolute_url())
    else:
        form = produccionForm()
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'p':p,'produccion':produccion,}

    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def producciones_esperadas(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    page_title = "Producciones Esperadas"
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_a_agendar__icontains=query) 
        )
        results = ProduccionEsperada.objects.filter(qset)
        template_name = "searchp.html"
        return render_to_response(template_name, {"results": results,"query": query,'empleado':empleado},context_instance=RequestContext(request)) 
    else:
        results = []
    template ="esperadas.html"
    produccion_e  = ProduccionEsperada.objects.filter(fecha_a_agendar=datetime.datetime.today)    
    args ={'produccion_e':produccion_e,'page_title':page_title,'empleado':empleado}

    return render_to_response(template, args,context_instance=RequestContext(request)) 

def esperada(request, produccione_id):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    produccion_e = get_object_or_404(ProduccionEsperada, id=produccione_id)
    page_title = produccion_e.producto.name
    if request.method == 'POST':
        form = produccionForm(request.POST , instance=produccion_e)
        if form.is_valid():
            produccion_e = form.save(commit = False)
            produccion_e.save()
            return redirect('producciones_esperadas')
    else:
        form = produccionForm(request.POST , instance=produccion_e)
        args = {}
        args.update(csrf(request))
        args ={'form':form,'produccion_e':produccion_e}
    template_name="esperada.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  

def produccion_realizada(request, producto_slug, template_name="produccion-realizada.html"):
    p 				= get_object_or_404(Product, slug=producto_slug)
    produccion 		= ProduccionRealizada.objects.all()
    page_title      = p.name
    produccion_e 	= ProduccionEsperada.objects.filter(producto=p,fecha_a_agendar__gt=datetime.datetime.today()- datetime.timedelta(days=3))
    produccion_rs    = ProduccionEsperada.objects.filter(producto=p,fecha_a_agendar=datetime.datetime.today() - datetime.timedelta(days=7))
    devolucion_r    = DevolucionReproceso.objects.filter(producto=p,fecha_de_entrada=datetime.datetime.today()- datetime.timedelta(days=1))
    if request.method == 'POST':
        form 			= produccionReForm(request.POST)
        formproducto 	= stockForm(request.POST , instance=p)
        if form.is_valid() and formproducto.is_valid():
            produccion     = form.save(commit = False)
            p = formproducto.save(commit = False)
            produccion.save()
            p.save()
            return redirect(p.get_absolute_url())
    else:
        form    = produccionReForm()
        formproducto = stockForm(request.POST , instance=p)
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'p':p,'produccion':produccion,'produccion_e':produccion_e}

    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def producciones_realizadas(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    page_title = "Producciones Realizadas"
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_de_elaboracion__icontains=query) 
        )
        results = ProduccionRealizada.objects.filter(qset)
        template_name = "search.html"
        return render_to_response(template_name, {"results": results,"query": query,'empleado':empleado},context_instance=RequestContext(request)) 
    else:
        results = []
    template ="realizadas.html"
    produccion_r  = ProduccionRealizada.objects.filter(fecha_de_elaboracion=datetime.datetime.today)    
    args ={'produccion_r':produccion_r,'page_title':page_title,'empleado':empleado}
    return render_to_response(template, args,context_instance=RequestContext(request)) 

def realizada(request, produccionr_id):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    produccion_r = get_object_or_404(ProduccionRealizada, id=produccionr_id)
    produccion_rs    = ProduccionRealizada.objects.filter(fecha_de_elaboracion__gte=datetime.datetime.today() - datetime.timedelta(days=7),fecha_de_elaboracion__lt=datetime.datetime.today())
    page_title = produccion_r.producto.name
    if request.method == 'POST':
        form = produccionReForm(request.POST , instance=produccion_r)
        formproducto    = stockForm(request.POST , instance=produccion_r.producto)
        if form.is_valid() and formproducto.is_valid():
            produccion_r = form.save(commit = False)
            formproducto.save(commit = False)
            produccion_r.save()
            formproducto.save()
            return redirect('producciones_realizadas')
    else:
        form = produccionReForm(request.POST , instance=produccion_r)
        formproducto = stockForm(request.POST , instance=produccion_r.producto)
    args = {}
    args.update(csrf(request))
    args ={'form':form,'produccion_r':produccion_r}
    template_name="realizada.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  
