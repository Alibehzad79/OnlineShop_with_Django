import itertools

from django.shortcuts import render
from django.views.generic import TemplateView

from shop_blog.models import Blog
from shop_products.models import Product
from shop_settings.models import Information
from shop_sliders.models import Slider
from shop_social_network.models import SocialNetwork


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request, *args, **kwargs):
    sliders = Slider.objects.all()
    product_by_special = Product.objects.filter(special=True).all()[:3]
    product_by_new = Product.objects.order_by("-id").all()[:4]
    product_by_view = Product.objects.order_by("-view").all()[:4]
    lasted_blog = Blog.objects.order_by("-id").all()[:2]
    context = {
        "product_special": my_grouper(3, product_by_special),
        "product_new": product_by_new,
        "product_view": my_grouper(4, product_by_view),
        'lasted_blog': lasted_blog,
        "sliders": sliders
    }
    return render(request, 'home_page.html', context)


def header(request):
    setting = Information.objects.first()
    context = {"setting": setting}
    return render(request, "shared/Header.html", context)


def footer(request):
    setting = Information.objects.first()
    context = {"setting": setting}
    return render(request, "shared/Footer.html", context)


def main_layout(request):
    setting = Information.objects.first()
    context = {"setting": setting}
    return render(request, "shared/Head.html", context)
