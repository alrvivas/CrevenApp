from django.db import models
from distutils.version import LooseVersion
from django.contrib.auth.models import User
from cliente.models import Cliente
from producto.models import Product
from orden.managers import OrderManager
from util.fields import CurrencyField
from jsonfield.fields import JSONField
from django.db.models.aggregates import Sum
from django.core.urlresolvers import reverse
import django
# Create your models here.
class Order(models.Model):
    objects = OrderManager()
    """
    A model representing an Order.

    An order is the "in process" counterpart of the shopping cart, which holds
    stuff like the shipping and billing addresses (copied from the User
    profile) when the Order is first created), list of items, and holds stuff
    like the status, shipping costs, taxes, etc...
    """

    PROCESSING = 10  # New order, addresses and shipping/payment methods chosen (user is in the shipping backend)
    CONFIRMING = 20  # The order is pending confirmation (user is on the confirm view)
    CONFIRMED = 30  # The order was confirmed (user is in the payment backend)
    COMPLETED = 40  # Payment backend successfully completed
    SHIPPED = 50  # The order was shipped to client
    CANCELED = 60  # The order was canceled
    CANCELLED = CANCELED  # DEPRECATED SPELLING

    PAYMENT = 30  # DEPRECATED!

    STATUS_CODES = (
        (PROCESSING, ('Procesando')),
        (CONFIRMING, ('Confirmando')),
        (CONFIRMED, ('Confirmada')),
        (COMPLETED, ('Completada')),
        (SHIPPED, ('Enviada')),
        (CANCELED, ('Cancelada')),
    )

    # If the user is null, the order was created with a session
    user 					= models.ForeignKey(User, blank=True, null=True, verbose_name=('User'))    
    cliente 				= models.ForeignKey(Cliente,null=True, blank=True)
    status 					= models.IntegerField(choices=STATUS_CODES, default=PROCESSING,verbose_name=('Status'))
    order_subtotal 			= CurrencyField(verbose_name=('Orden subtotal'))
    order_total 			= CurrencyField(verbose_name=('Orden Total'))
    order_totalpeso         = models.DecimalField(max_digits=10,decimal_places=3,null=True)
    shipping_address_text 	= models.TextField(('Direccion de Envio'), blank=True, null=True)
    billing_address_text	= models.TextField(('Direccion de Facturacion'), blank=True, null=True)
    created 				= models.DateTimeField(auto_now_add=True,verbose_name=('Creado'))
    modified 				= models.DateTimeField(auto_now=True, verbose_name=('Updated'))
    cart_pk 				= models.PositiveIntegerField(('Cart primary key'), blank=True, null=True)

    class Meta(object):
        verbose_name = ('Orden')
        verbose_name_plural = ('Ordenes')

    def __unicode__(self):
        return ('Orden ID: %(id)s') % {'id': self.pk}

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    def is_paid(self):
        """Has this order been integrally paid for?"""
        return self.amount_paid >= self.order_total
    is_payed = is_paid #Backward compatability, deprecated spelling

    def is_completed(self):
        return self.status == self.COMPLETED

    def get_status_name(self):
        return dict(self.STATUS_CODES)[self.status]

    @property
    def amount_paid(self):
        """
        The amount paid is the sum of related orderpayments
        """
        from .models import OrderPayment

        sum_ = OrderPayment.objects.filter(order=self).aggregate(sum=Sum('amount'))
        result = sum_.get('sum')
        if result is None:
            result = Decimal(0)
        return result
    amount_payed = amount_paid #Backward compatability, deprecated spelling

    @property
    def shipping_costs(self):
        from .models import ExtraOrderPriceField
        sum_ = Decimal('0.00')
        cost_list = ExtraOrderPriceField.objects.filter(order=self).filter(
                is_shipping=True)
        for cost in cost_list:
            sum_ += cost.value
        return sum_

    @property
    def short_name(self):
        """
        A short name for the order, to be displayed on the payment processor's
        website. Should be human-readable, as much as possible
        """
        return "%s-%s" % (self.pk, self.order_total)

    def set_billing_address(self, billing_address):
        """
        Process billing_address trying to get as_text method from address
        and copying.
        You can override this method to process address more granulary
        e.g. you can copy address instance and save FK to it in your order
        class.
        """
        if hasattr(billing_address, 'as_text') and callable(billing_address.as_text):
            self.billing_address_text = billing_address.as_text()
            self.save()

    def set_shipping_address(self, shipping_address):
        """
        Process shipping_address trying to get as_text method from address
        and copying.
        You can override this method to process address more granulary
        e.g. you can copy address instance and save FK to it in your order
        class.
        """
        if hasattr(shipping_address, 'as_text') and callable(shipping_address.as_text):
            self.shipping_address_text = shipping_address.as_text()
            self.save()

# We need some magic to support django < 1.3 that has no support
# models.on_delete option
f_kwargs = {}
if LooseVersion(django.get_version()) >= LooseVersion('1.3'):
    f_kwargs['on_delete'] = models.SET_NULL


class OrderItem(models.Model):
    """
    A line Item for an order.    """

    order 				= models.ForeignKey(Order, related_name='items',  verbose_name=('Orden'))
    product_reference 	= models.CharField(max_length=255,     verbose_name=('Product reference'))
    product_name 		= models.CharField(max_length=255, null=True, blank=True, verbose_name=('Product name'))
    product 			= models.ForeignKey(Product, verbose_name=('Producto'), null=True, blank=True, **f_kwargs)
    unit_price 			= CurrencyField(verbose_name=('Unit price'))
    quantity 			= models.IntegerField(verbose_name=('Cantidad'))
    line_subtotal		= CurrencyField(verbose_name=('Line subtotal'))
    line_total 			= CurrencyField(verbose_name=('Line total'))
    line_subtotalpeso 	= models.DecimalField(max_digits = 30,decimal_places = 3,null=True)
    line_totalpeso 		= models.DecimalField(max_digits = 30,decimal_places = 3,null=True)


    class Meta(object):
        verbose_name = ('Orden item')
        verbose_name_plural = ('Orden items')

    def save(self, *args, **kwargs):
        if not self.product_name and self.product:
            self.product_name = self.product.get_name()
        super(OrderItem, self).save(*args, **kwargs)


def clear_products(sender, instance, using, **kwargs):
    for oi in OrderItem.objects.filter(product=instance):
        oi.product = None
        oi.save()

if LooseVersion(django.get_version()) < LooseVersion('1.3'):
    pre_delete.connect(clear_products, sender=Product)


class OrderExtraInfo(models.Model):
    
    order = models.ForeignKey(Order, related_name="extra_info",verbose_name=('Order'))
    text = models.TextField(verbose_name=('Extra info'), blank=True)

    class Meta(object):
        verbose_name = ('Orden informacion extra')
        verbose_name_plural = ('Orden informacion extra')


class ExtraOrderPriceField(models.Model):
    """
    This will make Cart-provided extra price fields persistent since we want
    to "snapshot" their statuses at the time when the order was made
    """
    order 	= models.ForeignKey(Order, verbose_name=('Order'))
    label 	= models.CharField(max_length=255, verbose_name=('Label'))
    value 	= CurrencyField(verbose_name=('Amount'))
    data 	= JSONField(null=True, blank=True, verbose_name=('Serialized extra data'))
    # Does this represent shipping costs?
    is_shipping = models.BooleanField(default=False, editable=False, verbose_name=('Is shipping'))

    class Meta(object):
        verbose_name = ('Extra order price field')
        verbose_name_plural = ('Extra order price fields')


class ExtraOrderItemPriceField(models.Model):
    """
    This will make Cart-provided extra price fields persistent since we want
    to "snapshot" their statuses at the time when the order was made
    """
    order_item = models.ForeignKey(OrderItem, verbose_name=('Order item'))
    label = models.CharField(max_length=255, verbose_name=('Label'))
    value = CurrencyField(verbose_name=('Amount'))
    data = JSONField(null=True, blank=True, verbose_name=('Serialized extra data'))

    class Meta(object):
        verbose_name = ('Extra order item price field')
        verbose_name_plural = ('Extra order item price fields')


class OrderPayment(models.Model):
    """
    A class to hold basic payment information. Backends should define their own
    more complex payment types should they need to store more informtion
    """
    order = models.ForeignKey(Order, verbose_name=('Order'))
    # How much was paid with this particular transfer
    amount = CurrencyField(verbose_name=('Amount'))
    transaction_id = models.CharField(max_length=255, verbose_name=('Transaction ID'), help_text=("The transaction processor's reference"))
    payment_method = models.CharField(max_length=255, verbose_name=('Payment method'), help_text=("The payment backend used to process the purchase"))

    class Meta(object):
        verbose_name = ('Order payment')
        verbose_name_plural = ('Order payments')
