from django.db import models
from django.contrib.auth import get_user_model



class Order(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name='створено')
    user = models.ForeignKey(get_user_model(), blank=True, on_delete=models.CASCADE, verbose_name='користувач')
    done = models.BooleanField(default=False, verbose_name='статус')

    def __str__(self):
        formatted_date_time = self.created_at.strftime('%d %b %Y')
        return formatted_date_time

    def calculate_sum_weight(self):
        return round(sum(item.weight for item in self.orderitem_set.all()), 2)

    def calculate_sum_total(self):
        return round(sum(item.calculate_total() for item in self.orderitem_set.all()), 2)

    class Meta:
        verbose_name = 'замовлення'
        verbose_name_plural = 'замовлення'
        ordering = ['created_at', '-done']

