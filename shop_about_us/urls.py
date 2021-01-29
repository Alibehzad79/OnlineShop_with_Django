from django.urls import path

from shop_about_us.views import about_us

urlpatterns = [
    path("about-us", about_us)
]