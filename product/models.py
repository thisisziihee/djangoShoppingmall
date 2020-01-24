from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 32, verbose_name="상품명")
    price = models.IntegerField(verbose_name = "상품가격")
    description = models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고")
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Shoppingmall_Product"
        verbose_name = "상품"
        verbose_name_plural = "상품"