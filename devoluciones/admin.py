from django.contrib import admin
from .models import DevolucionBuena, DevolucionMala,DevolucionReproceso

@admin.register(DevolucionBuena)
class DevolucionBuenaAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_de_entrada','fecha_cracion')
	
@admin.register(DevolucionReproceso)
class DevolucionReprocesoAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_de_entrada','fecha_entrada')

@admin.register(DevolucionMala)
class DevolucionMalaAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_de_salida','fecha_cracion')