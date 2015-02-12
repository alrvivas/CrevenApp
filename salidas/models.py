from django.db import models
from producto.models import Product

class Salida(models.Model):
	producto 				= models.ForeignKey(Product)
	cantidad 				= models.IntegerField()
	fecha_cracion 			= models.DateTimeField(auto_now_add=True)
	fecha_de_salida 		= models.DateField(null=True,blank=True)

	def __unicode__(self):
	    return unicode(self.producto)

	@models.permalink
	def get_absolute_url(self):
		return ('salida', (), { 'salida_id': self.id })

	def totalhoy(self):
	    return self.cantidad + self.cantidad


	class Meta(object):
		ordering = ['-fecha_de_salida']
		verbose_name = ('Salida')
		verbose_name_plural = ('Salidas')

	
