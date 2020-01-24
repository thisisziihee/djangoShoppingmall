from django import forms
from .models import Order
from users.models import Users
from product.models import Product

class OrderForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
    
    quantity = forms.IntegerField(
        error_messages={'required':"수량을 입력하세요."},
        label = "수량"
    )
    product = forms.IntegerField(
        error_messages={'required':"상품을 입력하세요."},
        label = "상품", widget = forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

    
    if not(quantity and product and user):
        self.add_error('quantity', "수량이 없습니다.")
        self.add_error('product', "상품이 없습니다.")
