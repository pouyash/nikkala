from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from django.shortcuts import render

# Create your views here.
from django.views import View

from order.models import Order
from product.models import Category


class HomeView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'home/index.html', context)

def nav_component(request):
    categories_parent = Category.objects.filter(parent=None)
    context = {
        'categories_parent': categories_parent,
    }
    return render(request, 'utils/nav_component.html', context)

def footer_component(request):
    context = {

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
    print("*********************", count)
    context = {
        'order': order,
        'count':count,
    }
    return render(request, 'utils/header.html', context)