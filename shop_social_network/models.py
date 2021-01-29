from django.db import models


# Create your models here.

class SocialNetwork(models.Model):
    name = models.CharField(max_length=200, default="facebook")
    link = models.URLField(verbose_name="لینک")

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"

    def __str__(self):
        return self.name
