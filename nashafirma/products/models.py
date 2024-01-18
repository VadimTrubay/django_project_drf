from django.db import models


class Product(models.Model):
    product = models.CharField(max_length=100, verbose_name='продукт')
    price = models.FloatField(default=0, verbose_name='ціна')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукт'
        ordering = ['product', 'price']

    def __str__(self):
        return self.product
