from django.contrib import admin
from .models import Departamento,Empleado

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	list_filter = ('nombre',)
	search_fields = ('nombre',)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):	
	list_display = ('id','user','departamento','telefono',)
	list_display_links = ('user',) 
	list_filter = ('departamento',)
	list_per_page = 10
	search_fields = ('nombre','telefono')
	raw_id_fields = ('user','departamento')
	
	fields = ('user','departamento','telefono',)
	#list_editable = ('email','telefono',)
	

	#Cliente.allow_tags = Trueclass 
