from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
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
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity = form.data.get('quantity'),
                product = prod,
                user = Users.objects.get(email = self.request.session.get('user'))
            )
            print(order)
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


@method_decorator(login_required, name = 'dispatch')
class OrderList(ListView):
        # model = Order 을 해버리면 문제점이 뭐냐면, 로그인한 사용자에 대한 주문 정보만 나오면 되는데
        # 모든 사용자에 대한 주문 정보가 나온다. 그래서 session을 통해서 email 값을 받아오는 것이 필요하다.
        # queryset을 통해서 session 값 가져오는 것
    #model = Order
    template_name = "order.html"
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email = self.request.session.get('user'))
        return queryset

