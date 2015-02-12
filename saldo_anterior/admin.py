from django.contrib import admin
from .models import Saldo,Estatus

@admin.register(Estatus)
class EstatusAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Saldo)
class SaldoAdmin(admin.ModelAdmin):
	list_display 	= ('id','producto','cantidad','fecha_cracion')