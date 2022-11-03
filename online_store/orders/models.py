from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Order(models.Model):
    STATUS_TYPE_PAY = [
            ('o', 'online cart'),
            ('s', 'payment from someone else account'),
        ]

    STATUS_PAY = [
        ('p', 'purchased'),
        ('e', 'errors'),
        ('w', 'waiting for payment')
    ]

    TYPE_DELIVERY = [
        ('o', 'ordinary'),
        ('e', 'express'),
    ]

    user = models.ForeignKey(User, verbose_name='user', related_name='orders', on_delete=models.CASCADE)
    delivery = models.CharField(max_length=1, verbose_name='type delivery', choices=TYPE_DELIVERY, default='p')
    city = models.CharField(max_length=20, verbose_name='city')
    address = models.CharField(max_length=40, verbose_name='address')
    type_pay = models.CharField(max_length=1, choices=STATUS_TYPE_PAY, verbose_name='type pay', default='c')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_PAY, verbose_name='status pay', default='w')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='price', default=0)

    def status_pay_render(self):
        if self.status == 'o':
            return 'с онлайн карты'
        else:
            return 'с чужой карты'

    def type_pay_render(self):
        if self.type_pay == 'p':
            return 'оплачено'
        elif self.type_pay == 'e':
            return 'ошибка оплаты'
        else:
            return 'ожидает оплаты'

    def delivery_render(self):
        if self.delivery == 'o':
            return 'обычная доставка'
        else:
            return 'экспресс'

    def __str__(self):
        return f'order {self.id}'

    class Meta:
        ordering = ('-created',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name='order', on_delete=models.CASCADE)
    item = models.ForeignKey(Product, verbose_name='item', related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='price')
    quantity = models.PositiveIntegerField(default=1, verbose_name='quantity')

    def __str__(self):
        return f'order items {self.id}'
