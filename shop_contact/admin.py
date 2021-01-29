from django.contrib import admin

# Register your models here.
from shop_contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("__str__", "full_name", "is_read")
    list_editable = ("is_read",)
    search_fields = ("full_name",)
    list_filter = ("is_read",)
