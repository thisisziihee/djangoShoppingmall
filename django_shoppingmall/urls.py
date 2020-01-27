from django.contrib import admin
from django.urls import path
from users.views import home, RegisterView, LoginView, logout
from product.views import (
    ProductRegister, ProductList, ProductListAPI, ProductDetailAPI, ProductDetailView
)
from order.views import OrderCreate, OrderList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/',logout),
    path('product/register/', ProductRegister.as_view()),
    path('product/list/', ProductList.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('api/product/', ProductListAPI.as_view()),
    path('api/product/<int:pk>', ProductDetailAPI.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('order/', OrderList.as_view()),
]
