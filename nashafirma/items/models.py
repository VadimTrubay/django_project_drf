from django.db import models

from orders.models import Order
from products.models import Product


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='замовлення')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    weight = models.FloatField(default=0, verbose_name='вага')
    note = models.CharField(max_length=100, blank=True, verbose_name='нотатка')

    def __str__(self):
        return f'{self.order}'

    def calculate_total(self):
        return round(self.product.price * self.weight, 2)

    class Meta:
        verbose_name = 'продукти'
        verbose_name_plural = 'продукти'
        ordering = ['order__done', '-order__user']
