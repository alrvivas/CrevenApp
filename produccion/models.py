from django.db import models

from producto.models import Product

class ProduccionEsperada(models.Model):
	producto 		= models.ForeignKey(Product)
	cantidad 		= models.IntegerField()
	fecha_cracion 	= models.DateTimeField(auto_now_add=True)
	fecha_a_agendar = models.DateField(null=True,blank=True)
	realizada		= models.BooleanField(default=True)

	def __unicode__(self):
	    return "%s - %s"% (self.producto, self.fecha_a_agendar)

	class Meta(object):
		ordering = ['-fecha_a_agendar']
		verbose_name = ('Produccion Esperada')
		verbose_name_plural = ('Producciones Esperadas')

	@models.permalink
	def get_absolute_url(self):
		return ('esperada', (), { 'produccione_id': self.id })

	



class ProduccionRealizada(models.Model):
	producto 				= models.ForeignKey(Product)
	produccion_esperada		= models.ForeignKey(ProduccionEsperada)
	cantidad 				= models.IntegerField()
	fecha_cracion 			= models.DateTimeField(auto_now_add=True)
	fecha_de_elaboracion 	= models.DateField(null=True,blank=True)
	observacion 			= models.TextField(null=True,blank=True)

	def __unicode__(self):
	    return unicode(self.producto)

	class Meta(object):
		ordering = ['-fecha_de_elaboracion']
		verbose_name = ('Produccion Realizada')
		verbose_name_plural = ('Producciones Realizada')

	@models.permalink
	def get_absolute_url(self):
		return ('realizada', (), { 'produccionr_id': self.id })

	def produccion_kilos(self):
	    return self.producto.peso*self.cantidad

	def get_rendimiento(self):
	    return (float(self.cantidad)/float(self.produccion_esperada.cantidad))*100

	
