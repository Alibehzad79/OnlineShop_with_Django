from django.urls import path

from shop_contact.views import contact

urlpatterns = [
    path("contact", contact),
]