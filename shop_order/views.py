from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from shop_order.forms import NewUserOrderForm, SendRequestForm
from shop_order.models import Order, OrderDetail, SendRequest
from shop_products.models import Product
from shop_settings.models import Information


@login_required(login_url="/login")
def user_order(request):
    new_order_form = NewUserOrderForm(request.POST or None)

    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = new_order_form.cleaned_data.get("product_id")
        count = new_order_form.cleaned_data.get("count")
        if count <= 0:
            count = 1

        product = Product.objects.get_by_id(product_id=product_id)

        order.orderdetail_set.create(product_id=product.id, count=count, price=product.price)
        return redirect(f"products/{product.id}/{product.title.replace(' ', '-')}")
    return redirect("/")


@login_required(login_url="/login")
def order_detail_view(request):
    setting = Information.objects.first()
    context = {
        "setting": setting,
        "order": None,
        "order_detail": None,
        "price_total": None
    }
    order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is not None:
        context["order"] = order
        context["order_detail"] = order.orderdetail_set.all()
        context["price_total"] = order.get_total_price()

    return render(request, "order/order_detail.html", context)


@login_required(login_url='/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(pk=detail_id,
                                                              order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/order')
    raise Http404()


@login_required(login_url="/login")
def order_final(request):
    setting = Information.objects.first()

    send_request_form = SendRequestForm(request.POST or None)
    if send_request_form.is_valid():
        full_name = send_request_form.cleaned_data.get("full_name")
        phone = send_request_form.cleaned_data.get("phone")
        email = send_request_form.cleaned_data.get("email")
        address = send_request_form.cleaned_data.get("address")
        city = send_request_form.cleaned_data.get("city")
        postal_code = send_request_form.cleaned_data.get("postal_code")

        SendRequest.objects.create(full_name=full_name, phone=phone, email=email, address=address,
                                   city=city, postal_code=postal_code)
        send_request_form = SendRequestForm()
        return redirect("/")
    context = {
        "setting": setting,
        "send_request_form": send_request_form
    }

    return render(request, "order/order_final.html", context)
