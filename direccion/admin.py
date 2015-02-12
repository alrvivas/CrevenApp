from django.contrib import admin
from .models import Address, Estado

@admin.register(Estado)
class EstadotAdmin(admin.ModelAdmin):
	list_display 	= ('id','name')

@admin.register(Address)
class AddresstAdmin(admin.ModelAdmin):
	list_display 	= ('id','name','address','estado')