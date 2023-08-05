from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from django.shortcuts import render

# Create your views here.
from django.views import View

from blog.models import Blog
from order.models import Order
from product.models import Category, Product
from settings.models import Slider, AdvertiseTopIndex, AdvertiseMiddleIndex, AdvertiseBottomIndex, FooterCapability, \
    Footer, SocialMedia


class HomeView(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_active=True)
        top_ads = AdvertiseTopIndex.objects.filter(is_active=True).last()
        middle_ads = list(AdvertiseMiddleIndex.objects.filter(is_active=True).order_by('-id'))[0:4]
        bottom_ads = list(AdvertiseBottomIndex.objects.filter(is_active=True).order_by('-id'))[0:2]
        phones = list(Product.objects.filter(Q(category__title='موبایل') | Q(category__parent__title='موبایل'), is_active=True).order_by('-id'))[0:8]
        newest_products = list(Product.objects.filter(is_active=True).order_by('-id'))[0:6]
        newest_blogs = list(Blog.objects.filter(is_active=True).order_by('-id'))[0:6]
        context = {
            'sliders': sliders,
            'top_ads': top_ads,
            'middle_ads': middle_ads,
            'bottom_ads': bottom_ads,
            'phones': phones,
            'newest_products': newest_products,
            'newest_blogs': newest_blogs,
        }
        return render(request, 'home/index.html', context)


def nav_component(request):
    categories_parent = Category.objects.filter(parent=None)
    context = {
        'categories_parent': categories_parent,
    }
    return render(request, 'utils/nav_component.html', context)

def footer_component(request):
    footer_capabilities = list(FooterCapability.objects.filter(is_active=True).order_by('-id'))[0:5]
    footer = Footer.objects.prefetch_related('footer_images').filter(is_active=True).last()
    social_medias = SocialMedia.objects.filter(is_active=True)

    context = {
        'footer_capabilities': footer_capabilities,
        'footer': footer,
        'social_medias': social_medias,
    }
    return render(request, 'utils/footer_component.html', context)


def header_component(request):
    count = 0
    if request.user.is_authenticated:
        order:Order = Order.objects.prefetch_related('order_detail').filter(user=request.user, is_paid=False).first()
        count = Order.objects.aggregate(count_product=Sum('order_detail__count',filter=Q(user=request.user) & Q(is_paid=False)))


        if order == None:
            order = False
            count = 0
        else:
            count = count['count_product']
    else:
        order = False

    categories_parent = Category.objects.filter(parent=None)
    context = {
        'order': order,
        'count':count,
        'categories_parent':categories_parent,
    }
    return render(request, 'utils/header.html', context)