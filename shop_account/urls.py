from django.urls import path

from shop_account.views import log_out, login_page, register_page, user_panel, panel_edit # password_edit

urlpatterns = [
    path("login", login_page),
    path("register", register_page),
    path("panel", user_panel),
    path("panel/edit", panel_edit),
    # path("panel/edit/password", password_edit),
    path("log-out", log_out)
]

