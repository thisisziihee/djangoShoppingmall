from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from rest_framework import generics, mixins
from django.utils.decorators import method_decorator

from .models import Product
from .forms import RegisterForm
from order.forms import OrderForm
from users.decorators import admin_required
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

    # product_detail.html 에서 만든 폼을 전달해야하는데 
    # DetailView 에서 Form을 전달해야 해당하는 변수를 가지고 Form을 만든다?
    # 원하는 데이터를 넣을 수 있는 함수 추가
    # 폼을 생성할 때 self.request를 같이 넣어줘야한다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        print(context)
        return context