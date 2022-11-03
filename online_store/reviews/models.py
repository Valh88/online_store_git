from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Review(models.Model):
    review = models.TextField(max_length=1000, verbose_name='review')
    user = models.ForeignKey(User, related_name='reviews', verbose_name='user', on_delete=models.CASCADE, null=True,
                             blank=True)
    name = models.CharField(max_length=20, verbose_name='name of the reviewer')
    product = models.ForeignKey(Product, related_name='reviews', verbose_name='product', on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email')
    created = models.DateTimeField(auto_now_add=True, verbose_name='create data')

