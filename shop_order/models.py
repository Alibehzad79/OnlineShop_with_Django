from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from shop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده / نشده")
    paid_date = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید کاربران"

    def __str__(self):
        return self.owner.get_full_name()

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")

    class Meta:
        verbose_name = "جزییات سبد خرید"
        verbose_name_plural = "اطلاعات سبد های خرید کاربران"

    def __str__(self):
        return self.product.title

    def price_complete(self):
        return self.price * self.count


class SendRequest(models.Model):
    full_name = models.CharField(max_length=500, verbose_name="نام ونام خانوادگی")
    phone = models.CharField(max_length=15, verbose_name="تلفن")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")
    address = models.CharField(max_length=1000, verbose_name="آدرس")
    city = models.CharField(max_length=500, verbose_name="شهر")
    postal_code = models.CharField(max_length=25, verbose_name="کد پستی")

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست ها"

    def __str__(self):
        return self.full_name
