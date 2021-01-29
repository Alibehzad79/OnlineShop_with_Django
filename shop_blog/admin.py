from django.contrib import admin

# Register your models here.
from shop_blog.models import Blog, BlogForm


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("__str__", "author_name", "is_published")
    list_filter = ("is_published", "time")
    search_fields = ("title", "author_name")
    list_editable = ("is_published",)


@admin.register(BlogForm)
class BlogFormAdmin(admin.ModelAdmin):
    list_display = ("full_name", "is_read")
    list_filter = ("is_read",)
    search_fields = ("full_name",)
    list_editable = ("is_read",)

