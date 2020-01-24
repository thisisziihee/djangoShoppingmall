from django.shortcuts import render
from .models import Product
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from users.decorators import admin_required
from django.views.generic import ListView, DetailView
from rest_framework import generics, mixins
from .serializers import ProductSerializer

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        # 어떤 쿼리셋을 가져와야하는지 명시
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    #context_object_name = 'product_list'


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


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'