from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView
from .models import Order


class OrderListView(ListView):
	template_name = 'order_list.html'
	queryset = Order.objects.all()

	def get_queryset(self):
		queryset = super(OrderListView, self).get_queryset()
		queryset = queryset.filter(user=self.request.user)
		return queryset

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(OrderListView, self).dispatch(*args, **kwargs)


class OrderDetailView(DetailView):
    """
    Display order for logged in user.
    """
    template_name = 'order_detail.html'
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super(OrderDetailView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderDetailView, self).dispatch(*args, **kwargs)
