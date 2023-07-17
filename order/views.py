from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from order.models import Order, OrderDetail
from product.models import Product
from user.models import User
import json
import requests

@method_decorator(login_required, name='dispatch')
class AddToCardView(View):
    def get(self, request, slug):

        user: User = request.user
        product: Product = get_object_or_404(Product, slug=slug)

        order, created = Order.objects.get_or_create(user=user, is_paid=False)

        if created:
            OrderDetail.objects.create(order=order, product=product, count=1)

        else:
            od = OrderDetail.objects.filter(order=order, product=product)

            if len(od) == 1:
                od = od.first()
                od.count += 1
                od.save()
            else:

                OrderDetail.objects.create(order=order, product=product, count=1)


        return redirect(reverse('card'))


@method_decorator(login_required, name='dispatch')
class CardView(View):
    def get(self, request):
        user = request.user


        od:Order = Order.objects.prefetch_related('order_detail').filter(user=user, is_paid=False).first()


        context = {
            'ods': od
        }
        return render(request, 'order/card.html', context)



sandbox = 'sandbox'
MERCHANT = "00000000-0000-0000-0000-000000000000"
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
CallbackURL = 'http://127.0.0.1:8000/order/verify/'

@login_required
def send_request(request:HttpRequest):
    user_basket,created = Order.objects.get_or_create(is_paid=False,user=request.user)
    try:
        amount = user_basket.get_total_price() * 10
    except:
        return redirect(reverse('card'))

    data = {
        "MerchantID": MERCHANT,
        "Amount": amount,
        'Description':description,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                try:
                    return redirect(ZP_API_STARTPAY + str(response['Authority']),
                                    {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                                     'authority': response['Authority']})
                except:
                    return HttpResponse('FUCK YOU')
            else:
                return redirect(reverse('card'))
        return redirect(reverse('card'))

    except requests.exceptions.Timeout:
        return redirect(reverse('card'))
    except requests.exceptions.ConnectionError:
        return redirect(reverse('card'))


@login_required
def verify(request:HttpRequest):
    authority = request.GET.get('Authority')

    user_basket,created = Order.objects.get_or_create(is_paid=False,user=request.user)
    try:
        amount = user_basket.get_total_price() * 10
    except:
        return redirect(reverse('card'))
    data = {
        "MerchantID": MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)

    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:

            with transaction.atomic():
                for order_detail in user_basket.order_detail.all():
                    order_detail.total_price = order_detail.product.price * order_detail.count
                    order_detail.product.number -= order_detail.count
                    order_detail.product.save()
                    order_detail.save()
                user_basket.is_paid = True
                user_basket.payment_date = datetime.now()
                user_basket.save()
            return redirect(reverse('card'))
        else:
            return redirect(reverse('card'))
    return redirect(reverse('card'))