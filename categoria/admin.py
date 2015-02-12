from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display 	= ('id','slug','orden')
	list_editable 	= ('orden',)

	prepopulated_fields = {'slug' : ('nombre',)} 
