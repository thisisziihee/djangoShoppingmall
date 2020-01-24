from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(verbose_name="이메일", max_length = 128)
    password = models.CharField(max_length = 78, verbose_name = "비밀번호" )
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    level = models.CharField(verbose_name="사용자 등급", max_length=8,
    choices = (('admin', '관리자'), ('user', '일반 사용자')))

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Shoppingmall_users"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"

