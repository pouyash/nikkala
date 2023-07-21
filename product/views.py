from django.db.models import Q, Count, Sum
from django.shortcuts import render

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
