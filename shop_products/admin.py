from django.contrib import admin

# Register your models here.
from shop_products.models import Product, ProductForm, ProductGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "active")
    list_editable = ("active",)
    list_filter = ("title", "active")
    search_fields = ("title", "brand")


@admin.register(ProductForm)
class ProductFormAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_read")
    list_editable = ("is_read",)
    list_filter = ("is_read",)
    search_fields = ("full_name",)


admin.site.register(ProductGallery)
