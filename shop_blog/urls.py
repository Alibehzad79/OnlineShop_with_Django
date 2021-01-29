from django.urls import path

from shop_blog.views import BlogView, SearchBlog, blog_detail

urlpatterns = [
    path("blog", BlogView.as_view()),
    path("blog/search", SearchBlog.as_view()),
    path("blog/<blog_id>/<title>", blog_detail),
]