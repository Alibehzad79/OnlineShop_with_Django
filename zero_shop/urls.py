"""zero_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from zero_shop import settings
from zero_shop.views import home_page, main_layout, header, footer

urlpatterns = [
    path("", home_page),
    path("", include("shop_products.urls")),
    path("", include("shop_blog.urls")),
    path("", include("shop_about_us.urls")),
    path("", include("shop_order.urls")),
    path("", include("shop_contact.urls")),
    path("", include("shop_account.urls")),
    path("header", header, name='header'),
    path("footer", footer, name='footer'),
    path("head", main_layout, name='head'),
    path('admin/', admin.site.urls)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
