from django.contrib import admin

# Register your models here.
from shop_about_us.models import AboutUs, OurTeam

admin.site.register(AboutUs)


@admin.register(OurTeam)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("full_name",)
    search_fields = ("full_name",)
