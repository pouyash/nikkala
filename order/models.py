from django.db import models

from product.models import Product
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_total_price(self):
        result = 0
        if self.is_paid:
            for od in self.order_detail.all():
                result += od.total_price
        else:
            for od in self.order_detail.all():
                result += od.get_price()
        return result

    def __str__(self):
        return str(self.user) + " " + str(self.is_paid)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail', verbose_name='جزئیات سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_detail', verbose_name='محصول')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='تعداد')
    total_price = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='فیمت نهایی')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_price(self):
        return self.product.price * self.count

    class Meta:
        verbose_name = 'جزئیات'
        verbose_name_plural = 'جزئیات'

    def __str__(self):
        return str(self.order) + " " + str(self.product) + " " + str(self.count)