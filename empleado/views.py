from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Avg,Sum
from django.views.generic.base import View
from django.utils import timezone

from salidas.models import Salida
from devoluciones.models import DevolucionBuena
from models import *
import datetime


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def LoginView(request):
    if not request.user.is_anonymous():
        return redirect('index')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('index')
                else:
                    return render_to_response('inactivousuario.html', context_instance=RequestContext(request))#no activo
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))#no usuario
    else:
        formulario = AuthenticationForm()
    return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def index(request):
    page_title      = "Control de Inventarios"
    now             = timezone.now()
    _username       = request.user
    empleado        = Empleado.objects.filter(user= _username)
    salidas         = Salida.objects.filter(fecha_de_salida=datetime.datetime.today).aggregate(Sum('cantidad'))
    devoluciones_b  = DevolucionBuena.objects.filter(fecha_de_entrada=datetime.datetime.today).aggregate(Sum('cantidad'))
    args            = {}
    args            = {'page_title':page_title,'empleado':empleado,'salidas':salidas,'devoluciones_b':devoluciones_b}
    return render_to_response('index.html', args, context_instance=RequestContext(request))

