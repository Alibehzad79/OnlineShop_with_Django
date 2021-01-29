from django.db import models


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.CharField(max_length=500, verbose_name="توضیحات کوتاه")
    link = models.URLField(verbose_name="لینک")
    image = models.ImageField(upload_to="sliders", verbose_name="تصویر")

    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلاید ها"

    def __str__(self):
        return self.title
