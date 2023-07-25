import sweetify
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from sweetify.templatetags.sweetify import sweetify

from blog.forms import BlogCommentForm
from blog.models import Blog, CategoryBlog, CommentBlog


class BlogView(TemplateView):
    template_name = 'blog/index.html'


class BlogsView(ListView):
    template_name = 'blog/blogs.html'
    model = Blog
    context_object_name = "blogs"

    def get_queryset(self):
        cat = self.kwargs.get('cat')
        qs = super(BlogsView, self).get_queryset()
        qs = qs.filter(category__slug__icontains=cat)
        return qs




class BlogDetailView(DetailView):
    template_name = 'blog/blog.html'
    model = Blog
    context_object_name = 'blog'

    def get_queryset(self):
        cat = self.kwargs.get('slug')
        qs = super(BlogDetailView, self).get_queryset()
        qs = qs.filter(slug=cat)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogDetailView, self).get_context_data()
        context['forms'] = BlogCommentForm()
        context['comments'] = CommentBlog.objects.filter(is_active=True, parent=None).order_by('-id')
        return context

    def post(self, request, slug):

        blog = get_object_or_404(Blog, slug=slug)
        if request.user.is_authenticated:
            comment = request.POST.get("comment")
            CommentBlog.objects.create(
                name=request.user.username,
                email=request.user.email,
                blog=blog,
                comment=comment,
            )
        else:
            forms = BlogCommentForm(request.POST)
            if forms.is_valid():
                db = forms.save(commit=False)
                db.blog = blog
                db.save()

        return redirect(reverse('blog_detail', kwargs={'slug':slug}))


def nav_component(request):
    categories = CategoryBlog.objects.filter(is_active=True, parent=None)

    context = {
        "categories": categories,
    }
    return render(request, 'blog/utils/nav.html', context)


def footer_component(request):

    context = {

    }
    return render(request, 'blog/utils/footer_component.html', context)
