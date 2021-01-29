from django.db import models

# Create your models here.
from django.db.models import Q


class BlogManager(models.Manager):
    def get_boy_is_published(self):
        return self.get_queryset().filter(is_published=True)

    def get_by_id(self, blog_id):
        qs = self.get_queryset().filter(id=blog_id, is_published=True)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(author_name__icontains=query)
        )

        return self.get_queryset().filter(lookup, is_published=True).distinct()


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توصیحات")
    author_name = models.CharField(max_length=200, verbose_name="نام نویسنده")
    image = models.ImageField(upload_to="blog", verbose_name="تصویر")
    time = models.DateTimeField(verbose_name="زمان انتشار", blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name="منتشر شود / نشود")
    blog_visit = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    objects = BlogManager()

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"

    def __str__(self):
        return self.title

    def get_absolut_blog_url(self):
        return f'/blog/{self.id}/{self.title}'


class BlogForm(models.Model):
    blogId = models.IntegerField(default=1, verbose_name="بلاگ")
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    text = models.TextField(verbose_name="متن نظر")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده / نشده")

    class Meta:
        verbose_name = "نظرات"
        verbose_name_plural = "نطرات کاربران "

    def __str__(self):
        return self.full_name
