from django.db import models
from producto.models import Product

class Estatus(models.Model):
	nombre = models.CharField(max_length=255, verbose_name=('Nombre'))

	def __unicode__(self):
	    return self.nombre

class Saldo(models.Model):
	producto 			= models.ForeignKey(Product)
	cantidad 			= models.IntegerField()
	fecha_cracion 		= models.DateField(auto_now_add=True)
	fecha_de_entrada 	= models.DateField(null=True,blank=True)
	estatus 			= models.ForeignKey(Estatus)
	observacion 			= models.TextField(null=True,blank=True)


	@models.permalink
	def get_absolute_url(self):
		return ('saldo', (), { 'saldo_id': self.id })

	def get_kilos(self):
	    return self.producto.peso *self.cantidad


	class Meta(object):
		ordering = ['-fecha_cracion']
		verbose_name = ('Saldo')
		verbose_name_plural = ('Saldos')
