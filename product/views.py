from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from product.models import Product


class ProductsView(ListView):
    template_name = 'product/products.html'
    model = Product
    paginate_by = 1
    context_object_name = 'products'
    def get_queryset(self):
        qs = super(ProductsView, self).get_queryset()
        search = self.kwargs.get('search')
        qs = qs.filter(Q(brand__title__contains=search) | Q(category__title__contains=search))
        if len(qs) > 0:
            return qs
        else:
            return super(ProductsView, self).get_queryset()


class ProductDetailView(DetailView):
    template_name = 'product/product.html'
    context_object_name = 'product'
    model = Product
    slug_field = 'slug'
