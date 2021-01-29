from django.urls import path

from shop_products.views import product_detail, ProductListView, Search, ProductNew, ProductSpecial, ProductMostPopular

urlpatterns = [
    path("products", ProductListView.as_view()),
    path("products/search", Search.as_view()),
    path("products/special", ProductSpecial.as_view()),
    path("products/new", ProductNew.as_view()),
    path("products/most_popular", ProductMostPopular.as_view()),
    path("products/<productId>/<title>", product_detail),
]
