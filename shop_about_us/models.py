from django.db import models


# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "توضیحات درباره ما"

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="our_team", verbose_name="تصویر", blank=True, null=True)

    class Meta:
        verbose_name = "تیم ما"
        verbose_name_plural = "اعضای تیم ما"
