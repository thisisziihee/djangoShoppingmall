from django.shortcuts import render
from .models import Product
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from users.decorators import admin_required
from django.views.generic import ListView

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'


@method_decorator(admin_required, name = 'dispatch')
class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        product = Product(
            name = form.data.get('name'),
            price = form.data.get('price'),
            stock = form.data.get('stock'),
            description = form.data.get('description')
        )
        product.save()
        return super().form_valid(form)
