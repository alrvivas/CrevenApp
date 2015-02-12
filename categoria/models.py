from django.db import models

class Categoria(models.Model):
	nombre		= models.CharField(max_length=140)
	slug 		= models.SlugField(max_length=50, unique=True, help_text='Valor unico por producto URL pagina, creado desde nombre.',blank=True,null=True)
	es_activo 	= models.BooleanField(default=True)
	orden 		= models.PositiveIntegerField(null=True, blank=True)
	imagen 		= models.ImageField("Imagen Categoria", upload_to="images/categorias", blank=True, null=True)

	def imagen_categoria(self):
		return """<img src="%s" style="width:8em;" />""" % self.imagen.url

	imagen_categoria.allow_tags = True

	class Meta:
		ordering = ['orden']
		verbose_name_plural = 'Categorias' 

	def __unicode__(self): 
		return self.nombre

	@models.permalink
	def get_absolute_url(self):
		return ('catalogo_categoria', (), { 'categoria_slug': self.slug })