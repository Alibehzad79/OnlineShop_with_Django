import itertools

from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from shop_order.forms import NewUserOrderForm
from shop_products.forms import CreateProductForm
from shop_products.models import Product, ProductForm, ProductGallery


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.get_by_active()


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    product_id = kwargs["productId"]
    new_order_form = NewUserOrderForm(request.POST or None, initial={"product_id": product_id})
    product_form = CreateProductForm(request.POST or None, initial={"product_id": product_id})
    product = Product.objects.get_by_id(product_id)
    product.view += 1
    product.save()

    related_product: Product = Product.objects.get_queryset().filter(categories__product=product).all()

    if product_form.is_valid():
        full_name = product_form.cleaned_data.get("full_name")
        email = product_form.cleaned_data.get("email")
        text = product_form.cleaned_data.get("text")
        product_id = product_form.cleaned_data.get("product_id")

        product: Product = Product.objects.get_by_id(product_id=product_id)

        new_comment = ProductForm.objects.create(full_name=full_name, email=email, text=text,
                                                 productId=product.id)

        if new_comment is not None:
            return redirect(f"/products/{product.id}/{product.title}")
        product_form = CreateProductForm()

    comments = ProductForm.objects.filter(productId=product_id, is_read=True)
    gallery = ProductGallery.objects.filter(product_id=product_id).first()
    context = {
        "product": product,
        "comments": comments,
        "product_form": product_form,
        "related_product": related_product,
        "new_order_form": new_order_form,
        'gallery': gallery
    }
    return render(request, "products/product_detail.html", context)


class Search(ListView):
    template_name = "products/product_list.html"
    model = Product
    paginate_by = 8

    def get_queryset(self):
        request = self.request
        query = request.GET.get("q")
        if query is not None:
            return Product.objects.get_search(query)
        return Product.objects.get_by_active()


class ProductSpecial(ListView):
    template_name = "products/product_list.html"
    model = Product
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.filter(special=True, active=True).all()


class ProductNew(ListView):
    template_name = "products/product_list.html"
    model = Product
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.order_by("-id").all()


class ProductMostPopular(ListView):
    template_name = "products/product_list.html"
    model = Product
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.order_by("-view").all()
