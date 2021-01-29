from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from shop_blog.forms import CreateBlogForm
from shop_blog.models import Blog, BlogForm
from shop_settings.models import Information


class BlogView(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        return Blog.objects.get_boy_is_published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Information.objects.first()
        return context


def blog_detail(request, *args, **kwargs):
    settings = Information.objects.first()
    blog_id = kwargs["blog_id"]
    blog_form = CreateBlogForm(request.POST or None, initial={'blog_id': blog_id})
    blog: Blog = Blog.objects.get_by_id(blog_id)
    if blog is None:
        raise Http404()

    blog.blog_visit += 1
    blog.save()

    if blog_form.is_valid():
        full_name = blog_form.cleaned_data.get("full_name")
        email = blog_form.cleaned_data.get("email")
        text = blog_form.cleaned_data.get("text")
        blogId = blog_form.cleaned_data.get("blog_id")

        blog = Blog.objects.get_by_id(blog_id=blogId)

        new_comment = BlogForm.objects.create(full_name=full_name, email=email, text=text, blogId=blog.id)
        if new_comment is not None:
            return redirect(f"/blog/{blog.id}/{blog.title}")
        blog_form = CreateBlogForm()

    comments = BlogForm.objects.filter(blogId=blog_id, is_read=True)

    context = {
        "blog": blog,
        "setting": settings,
        "blog_form": blog_form,
        "comments": comments
    }
    return render(request, "blog/blog_detail.html", context)


class SearchBlog(ListView):
    template_name = "blog/blog_list.html"
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        query = request.GET.get("s")
        if query is not None:
            return Blog.objects.get_search(query)
        return Blog.objects.get_boy_is_published()
