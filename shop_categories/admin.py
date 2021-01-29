from django.contrib import admin

# Register your models here.
from shop_categories.models import Category

admin.site.register(Category)
