from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Q

from shop_categories.models import Category


class ProductManager(models.Manager):
    def get_by_active(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)

    def get_search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(brand__icontains=query) |
                Q(price__icontains=query) |
                Q(new_type__icontains=query) |
                Q(categories__name__icontains=query) |
                Q(categories__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    TYPE = (("جدید", "بله"), (" ", "خیر"))
    title: str = models.CharField(max_length=200, verbose_name="عنوان محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    price = models.IntegerField(default="1000", blank=True, null=True, verbose_name="قیمت")
    product_size = models.CharField(max_length=500, verbose_name="سایز محصول")
    color = models.CharField(max_length=200, verbose_name="رنگ", blank=True, null=True)
    image = models.ImageField(upload_to="products", blank=True, null=True, verbose_name="تصویر محصول")
    brand = models.CharField(max_length=200, verbose_name="برند")
    posting_details = models.CharField(max_length=500, default="", verbose_name="جزئیات ارسال")
    new_type = models.CharField(max_length=200, choices=TYPE, default="no", verbose_name="جدید")
    special = models.BooleanField(default=False, verbose_name="محصول ویژه")
    categories = models.ManyToManyField(Category, verbose_name="دسته بندی ها")
    active = models.BooleanField(default=False, verbose_name="موجود / ناموجود")
    view = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    objects = ProductManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"


class ProductForm(models.Model):
    productId = models.IntegerField(default=1, verbose_name="محصول")
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    text = models.TextField(verbose_name="متن نظر")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده / نشده")

    class Meta:
        verbose_name = "نظر کاربران"
        verbose_name_plural = "نطرات کاربران درباره محصولات"

    def __str__(self):
        return self.full_name


class ProductGallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    image_1 = models.ImageField(upload_to="Gallery", blank=True, null=True, verbose_name="تصویر اول")
    image_2 = models.ImageField(upload_to="Gallery", blank=True, null=True, verbose_name="تصویر دوم")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری ها"

    def __str__(self):
        return self.title
