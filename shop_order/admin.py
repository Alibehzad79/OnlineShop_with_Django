from django.contrib import admin

# Register your models here.
from shop_order.models import Order, OrderDetail, SendRequest


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_paid")
    list_editable = ("is_paid",)
    list_filter = ("is_paid",)
    search_fields = ("owner",)


admin.site.register(OrderDetail)
admin.site.register(SendRequest)
