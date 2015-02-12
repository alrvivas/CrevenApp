# -*- coding: utf-8 -*-
from shop_api import ShopAPI
from order_signals import payment_selection
from orden.models import Order,ExtraOrderPriceField
from django.shortcuts import redirect


class ShippingAPI(ShopAPI):
    def add_shipping_costs(self, order, label, value):
        """
        Add shipping costs to the given order, with the given label (text), and
        for the given value.
        Please not that the value *should* be negative (it's a cost).
        """
        # Check if we already have one shipping cost entry
        eopf = ExtraOrderPriceField.objects.filter(order=order,
                                                   is_shipping=True)
        if eopf and len(eopf) >= 1:
            eopf = eopf[0]

        if eopf:
            # Tweak the total (since the value might have changed)
            order.order_total = order.order_total - eopf.value

            # Update the existing fields
            eopf.label = label
            eopf.value = value
            eopf.save()

            # Re-add the shipping costs to the total
            order.order_total = order.order_total + value
            order.save()

        else:
            # In this case, there was no shipping cost already associated with
            # the order - let's simply create a new one (theat should be the
            # default case)
            ExtraOrderPriceField.objects.create(order=order,
                                                label=label,
                                                value=value,
                                                is_shipping=True)
            order.order_total = order.order_total + value
            order.save()

    def finished(self, order):
        """
        A helper for backends, so that they can call this when their job
        is finished i.e. shipping costs are added to the order.
        This will redirect to the "order confirmation" page.
        """
        order.status = Order.CONFIRMING
        order.save()
        # Emit the signal to say we're now selecting payment
        payment_selection.send(self, order=order)
        return redirect('checkout_confirm')
