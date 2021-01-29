from django.db import models


# Create your models here.

class Information(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان سایت")
    address = models.CharField(max_length=500, verbose_name="آدرس", blank=True, null=True)
    phone = models.CharField(max_length=25, verbose_name="شماره تماس", blank=True, null=True)
    fax = models.CharField(max_length=30, verbose_name="فکس", blank=True, null=True)
    email = models.EmailField(verbose_name="ایمیل", blank=True, null=True)
    map = models.ImageField(upload_to="map", blank=True, null=True, verbose_name="نقشه")
    logo = models.ImageField(upload_to="logo", verbose_name="لوگوی سایت(48*48)")
    description = models.TextField(verbose_name="توضیحات درباره سایت")
    copy_right = models.CharField(max_length=200, default=" ", verbose_name="متن کپی رایت")

    class Meta:
        verbose_name = "تنظیم سایت"
        verbose_name_plural = "تنظیم اطلاعات سایت"

    def __str__(self):
        return self.title


class WorkingHours(models.Model):
    day_name = models.CharField(max_length=200, verbose_name="روز")
    times = models.CharField(max_length=300, verbose_name="زمان", default="16:00 - 8:00 یا تعطیل")

    class Meta:
        verbose_name = "ساعت کاری"
        verbose_name_plural = "ساعات کاری"

    def __str__(self):
        return self.day_name
