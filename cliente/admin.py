from django.contrib import admin
from .models import Tipo_Cliente,Cliente

@admin.register(Tipo_Cliente)
class Tipo_ClienteAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre')