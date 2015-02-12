from django.db import models
from salidas.models import Salida
from devoluciones.models import DevolucionReproceso,DevolucionBuena,DevolucionMala
from produccion.models import ProduccionRealizada
"""
class Inventario(models.Model):
	fecha_creacion 			= models.DateTimeField(auto_now_add=True)
	salidas 				= models.ForeignKey(Salida)
	produccion 				= models.ForeignKey(ProduccionRealizada)
	devolucion_reproceso 	= models.ForeignKey(DevolucionReproceso)
	devolucion_buena		= models.ForeignKey(DevolucionBuena)
	devolucion_mala			= models.ForeignKey(DevolucionMala)

	def __unicode__(self): 
		return unicode(self.fecha_creacion)

	@models.permalink
	def get_absolute_url(self):
		return ('inventario', (), { 'inventario_id': self.id })

"""
