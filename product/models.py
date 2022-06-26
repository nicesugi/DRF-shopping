from turtle import up
from django.db import models


class Category(models.Model):
    name = models.CharField("카테고리", max_length=20)
    
class Product(models.Model):
    user = models.ForeignKey(to='user.User', verbose_name="사용자", on_delete=models.CASCADE)
    thumbnail = models.FileField("", upload_to="product/thumbnail/")
    detail = models.FileField("", upload_to="product/detail/")
    category = models.ForeignKey(to='Category', verbose_name="카테고리", null=True, on_delete=models.SET_NULL)
    title = models.CharField("제목", max_length=50)
    description = models.TextField("상품설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    
    def __str__(self):
        return f'({self.id}){self.title} / {self.user} 님이 등록하신 상품입니다'

class ProductOption(models.Model):
    product = models.ForeignKey(to='Product', verbose_name="상품", on_delete=models.CASCADE)
    name = models.CharField("옵션명", max_length=50)
    price = models.IntegerField("가격")

    def __str__(self):
        return f'{self.product}의 옵션입니다. / {self.name}, {self.price}원'

class Review(models.Model):
    product = models.ForeignKey(to='Product', verbose_name="상품", on_delete=models.CASCADE)
    user = models.ForeignKey(to='user.User', verbose_name="사용자", on_delete=models.CASCADE)
    rating = models.IntegerField("평점")
    content = models.TextField("리뷰내용")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    
    def __str__(self):
        return f'{self.product}의 리뷰입니다. 작성자: {self.name} 님'