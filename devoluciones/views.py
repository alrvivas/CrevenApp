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
from .models import DevolucionBuena, DevolucionMala, DevolucionReproceso
from .forms import devolucionForm, devolucionMalaForm,devolucionReprocesoForm
from producto.forms import stockForm
from django.core import urlresolvers
import datetime
from django.db.models import Q	

def add_devolucion_buena(request, producto_slug, template_name="add-devolucion-buena.html"):
    p = get_object_or_404(Product, slug=producto_slug)
    page_title = p.name
    devolucion_b 	= DevolucionBuena.objects.all()  
    if request.method == 'POST':
        form 			= devolucionForm(request.POST)
        formproducto 	= stockForm(request.POST , instance=p)
        if form.is_valid() and formproducto.is_valid():
            devolucion_b     = form.save(commit = False)
            p = formproducto.save(commit = False)
            devolucion_b.save()
            p.save()
            return redirect(p.get_absolute_url())
    else:
        form    = devolucionForm()
        formproducto = stockForm(request.POST , instance=p)
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'p':p,'devolucion_b':devolucion_b,}
    return render_to_response(template_name, locals(),context_instance=RequestContext(request)) 

def devoluciones_buenas(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    page_title 		= "Devoluciones Buenas"
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_de_entrada__icontains=query) 
        )
        results = DevolucionBuena.objects.filter(qset)
        template_name = "searchd.html"
        return render_to_response(template_name, {"results": results,"query": query,'empleado':empleado},context_instance=RequestContext(request)) 
    else:
        results = []
    template ="devoluciones-buenas.html"
    devolucion_b  	= DevolucionBuena.objects.filter(fecha_de_entrada=datetime.datetime.today)   
    args 			= {'devolucion_b':devolucion_b,'page_title':page_title,'empleado':empleado}
    return render_to_response(template, args,context_instance=RequestContext(request)) 

def devolucion_buena(request, devolucion_id):    
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    devolucion_b = get_object_or_404(DevolucionBuena, id=devolucion_id)
    page_title = devolucion_b.producto.name
    if request.method == 'POST':
        form = devolucionForm(request.POST , instance=devolucion_b)
        formproducto    = stockForm(request.POST , instance=devolucion_b.producto)
        if form.is_valid() and formproducto.is_valid():
            salida     = form.save(commit = False)
            formproducto.save(commit = False)
            salida.save()
            formproducto.save()
            return redirect('devoluciones_buenas')
    else:
        form = devolucionForm(request.POST , instance=devolucion_b)
        formproducto = stockForm(request.POST , instance=devolucion_b.producto)
    args = {}
    args.update(csrf(request))
    args ={'form':form,'devolucion_b':devolucion_b,}
    template_name="devolucion-buena.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  

def add_devolucion_mala(request, producto_slug, template_name="add-devolucion-mala.html"):
    p 				= get_object_or_404(Product, slug=producto_slug)
    devolucion_m 	= DevolucionMala.objects.all()
    page_title      = p.name
    #devolucion_b 	= ProduccionEsperada.objects.filter(producto=p,fecha_a_agendar__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    if request.method == 'POST':
        form 			= devolucionMalaForm(request.POST)
        #formproducto 	= stockForm(request.POST , instance=p)
        if form.is_valid() :
            devolucion_m     = form.save(commit = False)
            #p = formproducto.save(commit = False)
            devolucion_m.save()
            #p.save()
            return redirect(p.get_absolute_url())
    else:
        form    = devolucionMalaForm()
        #formproducto = stockForm(request.POST , instance=p)
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'p':p,'devolucion_m':devolucion_m,}

    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def devoluciones_malas(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    page_title = "Devoluciones Malas"
    devolucion_m  = DevolucionMala.objects.filter(fecha_de_salida=datetime.datetime.today)
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_de_salida__icontains=query) 
        )
        results = DevolucionMala.objects.filter(qset)
        template_name = "search.html"
        return render_to_response(template_name, {"results": results,"query": query,'empleado':empleado},context_instance=RequestContext(request)) 
    else:
        results = []  
    template ="devoluciones-malas.html"  
    args ={'devolucion_m':devolucion_m,'page_title':page_title,'empleado':empleado}
    return render_to_response(template, args,context_instance=RequestContext(request)) 

def devolucion_mala(request, devolucion_id):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    devolucion_m = get_object_or_404(DevolucionMala, id=devolucion_id)
    page_title = devolucion_m.producto.name
    if request.method == 'POST':
        form = devolucionMalaForm(request.POST , instance=devolucion_m)
        if form.is_valid():
            devolucion_m = form.save(commit = False)
            devolucion_m.save()
            return redirect('devoluciones_malas')
    else:
        form = devolucionMalaForm(request.POST , instance=devolucion_m)
        args = {}
        args.update(csrf(request))
        args ={'form':form,'devolucion_m':devolucion_m}
    template_name="devolucion-mala.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def add_devolucion_reproceso(request, producto_slug, template_name="add-devolucion-reproceso.html"):
    p 				= get_object_or_404(Product, slug=producto_slug)
    devolucion_r 	= DevolucionReproceso.objects.all()
    page_title      = p.name
    #devolucion_b 	= ProduccionEsperada.objects.filter(producto=p,fecha_a_agendar__lt=datetime.datetime.today()+ datetime.timedelta(days=1))
    if request.method == 'POST':
        form 			= devolucionReprocesoForm(request.POST)
        #formproducto 	= stockForm(request.POST , instance=p)
        if form.is_valid() :
            devolucion_r     = form.save(commit = False)
            #p = formproducto.save(commit = False)
            devolucion_r.save()
            #p.save()
            return redirect(p.get_absolute_url())
    else:
        form    = devolucionReprocesoForm()
        #formproducto = stockForm(request.POST , instance=p)
    args = {}
    args.update(csrf(request))    
    args ={'form':form,'p':p,'devolucion_r':devolucion_r,}

    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def devoluciones_reproceso(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    page_title = "Devoluciones De Reproceso"
    devolucion_r  = DevolucionReproceso.objects.filter(fecha_de_entrada=datetime.datetime.today)
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_de_entrada__icontains=query) 
        )
        results = DevolucionReproceso.objects.filter(qset)
        template_name = "searchd.html"
        return render_to_response(template_name, {"results": results,"query": query,'empleado':empleado},context_instance=RequestContext(request)) 
    else:
        results = []
    template ="devoluciones-reproceso.html"
    args ={'devolucion_r':devolucion_r,'page_title':page_title,'empleado':empleado}
    return render_to_response(template, args,context_instance=RequestContext(request)) 

def devolucion_reproceso(request, devolucion_id):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    devolucion_r = get_object_or_404(DevolucionReproceso, id=devolucion_id)
    page_title = devolucion_r.producto.name
    if request.method == 'POST':
        form = devolucionReprocesoForm(request.POST , instance=devolucion_r)
        if form.is_valid():
            devolucion_r = form.save(commit = False)
            devolucion_r.save()
            return redirect('devoluciones_reproceso')
    else:
        form = devolucionMalaForm(request.POST , instance=devolucion_r)
        args = {}
        args.update(csrf(request))
        args ={'form':form,'devolucion_r':devolucion_r}
    template_name="devolucion-reproceso.html"
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))  

