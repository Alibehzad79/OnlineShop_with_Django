from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

from shop_account.forms import RegisterForm, LoginForm, EditPanelForm


def login_page(request):
    if request.user.is_authenticated:
        redirect("/")

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error('user_name', "نام کاربری یا رمز عبور اشتباه می باشد")
    context = {
        "login_form": login_form
    }
    return render(request, "account/login.html", context)


def register_page(request):
    if request.user.is_authenticated:
        redirect("/")

    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect("/login")

    context = {
        "register_form": register_form
    }
    return render(request, "account/register.html", context)


def log_out(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login")
def user_sidebar(request):
    return render(request, "account/user_panel_partial.html", {})


@login_required(login_url="/login")
def panel_edit(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    edit_panel_form = EditPanelForm(request.POST or None,
                                    initial={"first_name": user.first_name, "last_name": user.last_name
                                             })
    if edit_panel_form.is_valid():
        first_name = edit_panel_form.cleaned_data.get("first_name")
        last_name = edit_panel_form.cleaned_data.get("last_name")
        user.first_name = first_name
        user.last_name = last_name
        user.save()
    context = {
        "edit_profile": edit_panel_form
    }
    return render(request, 'account/edit_profile.html', context)


@login_required(login_url="/login")
def user_panel(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    context = {
        "user": user
    }
    return render(request, "account/user_admin_panel.html", context)

# @login_required(login_url="/login")
# def password_edit(request):
#     user_id = request.user.id
#     user = User.objects.get(id=user_id)
#
#     edit_pass_form = EditPassForm(request.POST or None,
#                                   initial={"password": user.password, "re_password": user.password})
#     if edit_pass_form.is_valid():
#         password = edit_pass_form.cleaned_data.get("password")
#         re_password = edit_pass_form.cleaned_data.get("re_password")
#
#         User.password = password
#         return redirect("/login")
#
#     context = {
#         "edit_pass": edit_pass_form
#     }
#     return render(request, 'account/edit_password.html', context)
