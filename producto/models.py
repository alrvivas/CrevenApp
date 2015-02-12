from django.db import models
from util.fields import CurrencyField
from categoria.models import Categoria
from orden.managers import ProductManager,ProductStatisticsManager

class Product(models.Model):
	objects = ProductManager()
	statistics = ProductStatisticsManager()

	name 			= models.CharField(max_length=255, verbose_name=('Nombre'))
	slug 			= models.SlugField(verbose_name=('Slug'), unique=True)
	active 			= models.BooleanField(default=False, verbose_name=('Activo'))
	categoria 		= models.ForeignKey(Categoria)
	date_added		= models.DateTimeField(auto_now_add=True,verbose_name=('Fecha de Creacion'))
	last_modified 	= models.DateTimeField(auto_now=True,verbose_name=('Ultima Modificacion'))
	orden 			= models.PositiveIntegerField()
	stock			= models.IntegerField(blank=True)
	unit_price 		= CurrencyField(verbose_name=('Precio'))
	precio_a 		= CurrencyField(verbose_name=('Precio A'))
	precio_b 		= CurrencyField(verbose_name=('Precio B'))
	precio_c 		= CurrencyField(verbose_name=('Precio C'))
	peso 			= models.DecimalField(max_digits = 30,decimal_places = 2,)
	imagen 			= models.ImageField("Imagen Categoria", upload_to="images/categorias", blank=True, null=True,default='images/default-01.png')


	class Meta(object):
		ordering = ['orden']
		verbose_name = ('Producto')
		verbose_name_plural = ('Productos')

	def __unicode__(self):
	    return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('product_detail', (), { 'producto_slug': self.slug })

	@models.permalink
	def get_absolute_urlpe(self):
		return ('produccion_esperada', (), { 'producto_slug': self.slug })

	@models.permalink
	def get_absolute_urlpr(self):
		return ('produccion_realizada', (), { 'producto_slug': self.slug })

	@models.permalink
	def get_absolute_urldb(self):
		return ('add_devolucion_buena', (), { 'producto_slug': self.slug })

	@models.permalink
	def get_absolute_urldm(self):
		return ('add_devolucion_mala', (), { 'producto_slug': self.slug })

	@models.permalink
	def get_absolute_urldr(self):
		return ('add_devolucion_reproceso', (), { 'producto_slug': self.slug })

	@models.permalink
	def get_absolute_urlsa(self):
		return ('add_salida', (), { 'producto_slug': self.slug })

	@models.permalink
	def get_absolute_urlsal(self):
		return ('add_saldo', (), { 'producto_slug': self.slug })


	def get_price(self):
	    return self.unit_price

	def get_peso(self):
	    return self.peso

	def get_subtotal(self):
	    return self.peso *self.stock

	def get_name(self):
	    return self.name

	def get_product_reference(self):
		return unicode(self.pk)

	@property
	def can_be_added_to_cart(self):
	    return self.active