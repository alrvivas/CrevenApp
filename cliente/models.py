from django.db import models
from django.contrib.auth.models import User

class Tipo_Cliente(models.Model):
	nombre		= models.CharField(max_length=140)

	def __unicode__(self): 
		return self.nombre

class Cliente(models.Model):
	user 		= models.ForeignKey(User, unique=True)
	nombre		= models.CharField(max_length=140)
	tipo 		= models.ForeignKey(Tipo_Cliente)

	def __unicode__(self): 
		return self.nombre


