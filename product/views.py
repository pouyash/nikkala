from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Sum
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView

from product.models import Product, Category, Brand


class ProductsView(ListView):
    template_name = 'product/products.html'
    model = Product
    paginate_by = 1
    context_object_name = 'products'

    def get_queryset(self):

        qs = super(ProductsView, self).get_queryset()
        product_search = self.request.GET.get('product_search')
        if product_search:
            qs = qs.filter(Q(title__icontains=product_search) | Q(category__title__icontains=product_search) | Q(brand__title__icontains=product_search))
            return qs

        if self.request.path == '/product/order/most_buy/':
            order = self.kwargs.get('order')
            if order == 'most_buy':
                qs = qs.annotate(most_buy=Sum('order_detail__count',default=0)).order_by('-most_buy')
                return qs
        elif self.request.path == '/product/order/newest/':
            order = self.kwargs.get('order')
            if order == 'newest':
                qs = qs.order_by('-id')
                return qs
        elif self.request.path == '/product/order/cheaper/':
            order = self.kwargs.get('order')
            if order == 'cheaper':
                qs = qs.order_by('price')
                return qs
        elif self.request.path == '/product/order/expensive/':
            order = self.kwargs.get('order')
            if order == 'expensive':
                qs = qs.order_by('-price')
                return qs
        else:
            search = self.kwargs.get('search')
            qs = qs.filter(Q(brand__title__contains=search) | Q(category__title__contains=search))
            if len(qs) > 0:
                return qs
            else:
                return super(ProductsView, self).get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data()
        context['category_parent'] = Category.objects.filter(parent=None)
        context['brands'] = Brand.objects.all()
        return context

class ProductDetailView(DetailView):
    template_name = 'product/product.html'
    context_object_name = 'product'
    model = Product
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context['has_favorite'] = False
        if self.request.user.is_authenticated:
            slug = self.kwargs.get('slug')
            product = Product.objects.get(slug=slug)
            user = self.request.user
            if product.user_like.filter(id=user.id):
                context['has_favorite'] = True
        return context

@login_required
def add_product_to_favorite(request:HttpRequest, id):
    user = request.user
    product_exists = Product.objects.filter(id=id).exists()
    if product_exists:
        product = Product.objects.filter(id=id).first()
        check = product.user_like.filter(id=user.id).exists()
        if check:
            product.user_like.remove(user)
            product.save()
        else:
            product.user_like.add(user)
            product.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))