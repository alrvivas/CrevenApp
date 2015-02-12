from django.contrib import admin
from .models import Salida


@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_de_salida','fecha_cracion')
	list_filter 	= ('fecha_de_salida','fecha_cracion',)
