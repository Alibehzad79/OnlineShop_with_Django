from django.urls import path

from shop_order.views import user_order, order_detail_view, order_final, remove_order_detail

urlpatterns = [
    path("add-user-order", user_order),
    path("add-user-order/", user_order),
    path("order", order_detail_view),
    path("order/", order_detail_view),
    path("remove-item/<detail_id>", remove_order_detail),
    path("remove-item/<detail_id>/", remove_order_detail),
    path("order/final", order_final),
    path("order/final/", order_final),
]
