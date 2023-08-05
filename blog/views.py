import time

import sweetify
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from sweetify.templatetags.sweetify import sweetify

from blog.forms import BlogCommentForm
from blog.models import Blog, CategoryBlog, CommentBlog, BlogBanner
from settings.models import SocialMedia


class BlogView(ListView):
    template_name = 'blog/index.html'
    model = Blog
    context_object_name = "blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogView, self).get_context_data()
        context['left_sides'] = list(Blog.objects.filter(is_active=True))[0:2]
        context['techs'] = Blog.objects.filter(Q(category__title__contains='تکنولوژی') | Q(category__parent__title__contains='تکنولوژی'))
        return context


class BlogsView(ListView):
    template_name = 'blog/blogs.html'
    model = Blog
    context_object_name = "blogs"
    paginate_by = 2

    def get_queryset(self):
        cat = self.kwargs.get('cat')
        qs = super(BlogsView, self).get_queryset()
        if cat != 'all':
            qs = qs.filter(category__slug__icontains=cat)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogsView, self).get_context_data()
        context['banner'] = BlogBanner.objects.filter(is_active=True).last()
        return context





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
        blog_slug = self.kwargs.get('slug')
        context['comments'] = CommentBlog.objects.filter(is_active=True, parent=None, blog__slug=blog_slug).order_by('-id')
        blog = Blog.objects.get(slug=blog_slug)
        context['recommends'] = set(Blog.objects.filter(Q(category__slug__icontains=blog.category.slug) | Q(tags__in=blog.tags.all())).exclude(id=blog.id))
        blog = Blog.objects.get(slug=blog_slug)
        id = blog.id
        ip = self.request.META.get('REMOTE_ADDR')
        if self.request.COOKIES.get(str(id)) == str(ip):
            context['has_favorite'] = True
        else:
            context['has_favorite'] = False
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

        return redirect(reverse('blog_detail', kwargs={'slug': slug}))


@login_required
def blog_comment_like(request, comment_id):
    user = request.user
    comment_exists = CommentBlog.objects.filter(id=comment_id).exists()
    if comment_exists:
        comment = CommentBlog.objects.get(id=comment_id)
        if user in comment.user_reaction.all():
            comment.user_reaction.remove(user)
            comment.like_count -= 1
            comment.save()
        else:
            comment.user_reaction.add(user)
            comment.like_count += 1
            comment.save()

        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect(reverse('blogs'))



def add_session(request:HttpRequest, id):
    client_ip = request.META.get('REMOTE_ADDR')
    blog_exists = Blog.objects.filter(id=id).exists()
    if blog_exists:
        response = redirect(request.META.get('HTTP_REFERER'))

        if request.COOKIES.get(str(id)) == str(client_ip):
            response.delete_cookie(str(id))
        else:
            response.set_cookie(id, client_ip, 3600 * 24)

        return response
    else:
        return redirect(request.META.get('HTTP_REFERER'))


def nav_component(request):
    categories = CategoryBlog.objects.filter(is_active=True, parent=None)

    context = {
        "categories": categories,
    }
    return render(request, 'blog/utils/nav.html', context)





def footer_component(request):
    social_medias = SocialMedia.objects.filter(is_active=True)
    context = {
        'social_medias': social_medias,
    }
    return render(request, 'blog/utils/footer_component.html', context)
