from django.contrib import admin
from django.contrib.admin import register

from blog.models import Blog, CategoryBlog, Tag, CommentBlog


@register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'parent', 'is_active']

    prepopulated_fields = {
        'slug': ('title',)
    }


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'is_active']

    prepopulated_fields = {
        'slug': ('title',)
    }


@register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'user', 'category', 'is_active']
    prepopulated_fields = {
        'slug': ('title',)
    }

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BlogAdmin, self).save_model(request, obj, form, change)


@register(CommentBlog)
class CommentBlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'parent', 'is_active', 'like_count']






