from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
      
    
class User(AbstractBaseUser):
    username = models.CharField("사용자계정", max_length=50, unique=True)
    # email = models.EmailField("이메일", unique=True)
    password = models.CharField("비밀번호", max_length=256)
    fullname = models.CharField("이름", max_length=50)
    phone = models.CharField("핸드폰번호", max_length=20)
    
    is_active = models.BooleanField("계정 활성화 여부", default=True)
    is_admin = models.BooleanField("admin 권한", default=False)
    
    cart = models.ManyToManyField(to='product.ProductOption', verbose_name="장바구니", through='Cart', related_name="carts" )
    keep = models.ManyToManyField(to='product.Product', verbose_name="찜 상품", related_name="keeps")
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, perm, obj=None):
        return True
    
    @property
    def is_staff(self):
        return self._is_admin
    
    
class Celler(models.Model):
    user = models.OneToOneField(to='User', verbose_name="사용자", on_delete=models.CASCADE)
    approval_date = models.DateTimeField("승인일자", null=True)
    
    
class Cart(models.Model):
    user = models.ForeignKey(to='User', verbose_name="사용자",  related_name="users", on_delete=models.CASCADE)
    product_option = models.ForeignKey(to='product.ProductOption', verbose_name="상품옵션",on_delete=models.CASCADE)
    count = models.IntegerField("수량")
    
    
class PurchaseList(models.Model):
    STATUS = (
        ("ready", "배송 준비 중"),
        ("delivery", "배송 중"),
        ("done", "배송 완료"),
    )
    
    user = models.ForeignKey(to='User', verbose_name="사용자", on_delete=models.CASCADE)
    count = models.IntegerField("수량")
    status = models.CharField("배송 상태", choices=STATUS, max_length=10)
    
    
class PurchaseHistory(models.Model):
    PAYMENT_TYPE = (
        ("card", "카드"),
        ("cash", "무통장 입금"),
    )
    
    purchase_list = models.ManyToManyField(to='PurchaseList', verbose_name="구매목록")
    payment_type = models.CharField("결제방식", choices=PAYMENT_TYPE, max_length=50)
    payment_datetime = models.DateTimeField("결제일시", auto_now_add=True)
    