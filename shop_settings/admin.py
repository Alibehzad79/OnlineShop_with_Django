from django.contrib import admin

# Register your models here.
from shop_settings.models import Information, WorkingHours

admin.site.register(Information)
admin.site.register(WorkingHours)
