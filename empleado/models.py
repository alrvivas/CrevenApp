from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
	nombre 		= models.CharField(max_length=140)

	def __unicode__(self): 
		return unicode(self.nombre)

class Empleado(models.Model):
	user 			= models.ForeignKey(User, unique=True)
	departamento 	= models.ForeignKey(Departamento, blank=True, null=True)
	telefono 		= models.PositiveIntegerField(null=True, blank=True)

	def __unicode__(self): 
		return unicode(self.user)