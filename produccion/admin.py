from django.contrib import admin
from models import ProduccionEsperada, ProduccionRealizada

@admin.register(ProduccionEsperada)
class ProduccionEsperadaAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_cracion','fecha_a_agendar')
	list_editable 	= ('fecha_a_agendar',)
	

@admin.register(ProduccionRealizada)
class ProduccionRealizadaAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_de_elaboracion','fecha_cracion')
	list_editable 	= ('fecha_de_elaboracion',)
	