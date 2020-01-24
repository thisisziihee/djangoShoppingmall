from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.db import transaction

from .forms import OrderForm
from .models import Order
from users.models import Users
from product.models import Product
from users.decorators import login_required


@method_decorator(login_required, name = 'dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/list'

    def form_valid(self, form):
        with transaction.atomic():
            prod = Product.objects.gt(pk=form.data.get('product'))
            order = Order(
                quantity = form.data.get('quantity'),
                product = prod,
                user = Users.objects.get(email = self.request.session.get('user'))
            )
            order.save()

            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)

    
    def form_invalid(self, form):
        return redirect('/product/'+str(form.data.get('product')))
    

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request':self.request
        })
        return kw


