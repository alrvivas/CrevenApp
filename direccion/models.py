from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente
from django.conf import settings

BASE_ADDRESS_TEMPLATE = \
("""
Nombre: %(name)s,
Direccion: %(address)s,
C.P: %(zipcode)s,
Ciudad: %(city)s,
Estado: %(estado)s
""")

ADDRESS_TEMPLATE = getattr(settings, 'SHOP_ADDRESS_TEMPLATE',
                           BASE_ADDRESS_TEMPLATE)
class Estado(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta(object):
        verbose_name = ('Estado')
        verbose_name_plural = ('Estados')


class Address(models.Model):
    user_shipping = models.OneToOneField(User, related_name='shipping_address',
                                         blank=True, null=True)
    user_billing = models.OneToOneField(User, related_name='billing_address',
                                        blank=True, null=True)

    name = models.CharField(('Name'), max_length=255)
    address = models.CharField(('Direccion '), max_length=255)
    address2 = models.CharField(('Direccion2'), max_length=255, blank=True)
    zip_code = models.CharField(('C.P.'), max_length=20)
    city = models.CharField(('Ciudad'), max_length=20)
    estado = models.ForeignKey(Estado, verbose_name=('Estado'), blank=True, null=True)

    class Meta(object):
        verbose_name = ('Direccion')
        verbose_name_plural = ("Direcciones")

    def __unicode__(self):
        return '%s (%s, %s)' % (self.name, self.zip_code, self.city)

    def clone(self):
        new_kwargs = dict([(fld.name, getattr(self, fld.name))
                           for fld in self._meta.fields if fld.name != 'id'])
        return self.__class__.objects.create(**new_kwargs)

    def as_text(self):
        return ADDRESS_TEMPLATE % {
            'name': self.name,
            'address': '%s\n%s' % (self.address, self.address2),
            'zipcode': self.zip_code,
            'city': self.city,
            'estado': self.estado,
        }

  