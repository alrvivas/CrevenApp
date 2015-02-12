# -*- coding: utf-8 -*-
from django.conf import settings
from decimal import Decimal
from django.db import models
from distutils.version import LooseVersion
from cliente.models import Cliente
#from .models import CartItem
from producto.models import Product
from cart.modifiers_pool import cart_modifiers_pool
from util.fields import CurrencyField
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from django.core.urlresolvers import reverse
import django
import decimal
from polymorphic.polymorphic_model import PolymorphicModel


class Cart(models.Model):
    """
    This should be a rather simple list of items. Ideally it should be bound to
    a session and not to a User is we want to let people buy from our shop
    without having to register with us.
    """
    # If the user is null, that means this is used for a session
    user = models.ForeignKey(User, null=True, blank=True)
    cliente = models.ForeignKey(Cliente,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta(object):
    	ordering = ['date_created']
        verbose_name = ('Carro')
        verbose_name_plural = ('Carros')

    def __init__(self, *args, **kwargs):
        super(Cart, self).__init__(*args, **kwargs)
        # That will hold things like tax totals or total discount
        self.subtotal_price = decimal.Decimal('0.00')
        self.total_price = decimal.Decimal('0.00')
        self.subtotal_peso = decimal.Decimal('0.000')
        self.total_peso = decimal.Decimal('0.000')
        self.current_total = decimal.Decimal('0.00')  # used by cart modifiers
        self.extra_price_fields = []  # List of tuples (label, value)
        self._updated_cart_items = None

    def add_product(self, product, quantity=1, merge=True, queryset=None):
       
        from .models import CartItem

        # check if product can be added at all
        if not getattr(product, 'can_be_added_to_cart', True):
            return None

        # get the last updated timestamp
        # also saves cart object if it is not saved
        self.save()

        if queryset is None:
            queryset = CartItem.objects.filter(cart=self, product=product)
        item = queryset
        # Let's see if we already have an Item with the same product ID
        if item.exists() and merge:
            cart_item = item[0]
            cart_item.quantity = cart_item.quantity + int(quantity)
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(
                cart=self, quantity=quantity, product=product)
            cart_item.save()

        return cart_item

    def update_quantity(self, cart_item_id, quantity):
        
        cart_item = self.items.get(pk=cart_item_id)
        if quantity == 0:
            cart_item.delete()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        self.save()
        return cart_item

    def delete_item(self, cart_item_id):
        """
        A simple convenience method to delete one of the cart's items. This
        allows to implicitely check for "access rights" since we insure the
        cartitem is actually in the user's cart
        """
        cart_item = self.items.get(pk=cart_item_id)
        cart_item.delete()
        self.save()

    def get_updated_cart_items(self):
        """
        Returns updated cart items after update() has been called and
        cart modifiers have been processed for all cart items.
        """
        assert self._updated_cart_items is not None, ('Cart needs to be '
            'updated before calling get_updated_cart_items.')
        return self._updated_cart_items

    def update(self, request):
        """
        This should be called whenever anything is changed in the cart (added
        or removed).
        It will loop on all line items in the cart, and call all the price
        modifiers on each row.
        After doing this, it will compute and update the order's total and
        subtotal fields, along with any payment field added along the way by
        modifiers.

        Note that theses added fields are not stored - we actually want to
        reflect rebate and tax changes on the *cart* items, but we don't want
        that for the order items (since they are legally binding after the
        "purchase" button was pressed)
        """
        

        # This is a ghetto "select_related" for polymorphic models.
        items = CartItem.objects.filter(cart=self)
        product_ids = [item.product_id for item in items]
        products = Product.objects.filter(pk__in=product_ids)
        products_dict = dict([(p.pk, p) for p in products])

        self.extra_price_fields = []  # Reset the price fields
        self.subtotal_price = decimal.Decimal('0.00')  # Reset the subtotal
        self.subtotal_peso = decimal.Decimal('0.000')

        # The request object holds extra information in a dict named 'cart_modifier_state'.
        # Cart modifiers can use this dict to pass arbitrary data from and to each other.
        if not hasattr(request, 'cart_modifier_state'):
            setattr(request, 'cart_modifier_state', {})

        # This calls all the pre_process_cart methods (if any), before the cart
        # is processed. This allows for data collection on the cart for
        # example)
        for modifier in cart_modifiers_pool.get_modifiers_list():
            modifier.pre_process_cart(self, request)

        for item in items:  # For each CartItem (order line)...
            # This is still the ghetto select_related
            item.product = products_dict[item.product_id]
            self.subtotal_price = self.subtotal_price + item.update(request)
            self.subtotal_peso  = self.subtotal_peso + item.updatepeso(request)

        self.current_total = self.subtotal_price
        

        # Now we have to iterate over the registered modifiers again
        # (unfortunately) to pass them the whole Order this time
        for modifier in cart_modifiers_pool.get_modifiers_list():
            modifier.process_cart(self, request)

        self.total_price = self.current_total
        self.total_peso = self.subtotal_peso

        # This calls the post_process_cart method from cart modifiers, if any.
        # It allows for a last bit of processing on the "finished" cart, before
        # it is displayed
        for modifier in cart_modifiers_pool.get_modifiers_list():
            modifier.post_process_cart(self, request)

        # Cache updated cart items
        self._updated_cart_items = items

    def empty(self):
        """
        Remove all cart items
        """
        if self.pk:
            self.items.all().delete()
            self.delete()

    @property
    def total_quantity(self):
        """
        Returns the total quantity of all items in the cart
        """
        return sum([ci.quantity for ci in self.items.all()])


class CartItem(models.Model):
    """
    This is a holder for the quantity of items in the cart and, obviously, a
    pointer to the actual Product being purchased :)
    """
    cart = models.ForeignKey(Cart, related_name="items")

    quantity = models.IntegerField()

    product = models.ForeignKey(Product)

    class Meta(object):
        verbose_name = ('Cart item')
        verbose_name_plural = ('Cart items')

    def __init__(self, *args, **kwargs):
        super(CartItem, self).__init__(*args, **kwargs)
        self.extra_price_fields = [] 
        self.line_subtotal = decimal.Decimal('0.00')
        self.line_total = decimal.Decimal('0.00')
        self.current_total = decimal.Decimal('0.00')  # Used by cart modifiers
        self.line_subtotalpeso = decimal.Decimal('0.000')
        self.line_totalpeso = decimal.Decimal('0.00')

    def update(self, request):
        self.extra_price_fields = []  # Reset the price fields
        self.line_subtotal = self.product.get_price() * self.quantity
        self.current_total = self.line_subtotal

        for modifier in cart_modifiers_pool.get_modifiers_list():
            # We now loop over every registered price modifier,
            # most of them will simply add a field to extra_payment_fields
            modifier.process_cart_item(self, request)

        self.line_total = self.current_total
        return self.line_total

    def updatepeso(self, request):
        self.line_subtotalpeso = self.product.get_peso() * self.quantity
        
        self.line_totalpeso = self.line_subtotalpeso
        return self.line_totalpeso
    