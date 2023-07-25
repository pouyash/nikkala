import sweetify
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.generic import ListView, DetailView
from requests import post

from order.models import Order, OrderDetail
from utils.functions import create_activation_code
# Create your views here.
from django.urls import reverse
from django.views import View

from account.forms import RegisterForm, LoginForm, ChangePasswordForm
from user.models import User
from utils.email import send_email

class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        forms = RegisterForm()

        context = {
            'forms': forms
        }
        return render(request, 'account/register.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        check = request.POST.get('check')
        if check == 'on':
            forms = RegisterForm(request.POST)
            if forms.is_valid():
                user: User = User.objects.create(
                    username=forms.cleaned_data.get('name'),
                    email=forms.cleaned_data.get('email'),
                )
                user.set_password(forms.cleaned_data.get('password'))
                code = create_activation_code()
                user.activated_code = code
                user.save()
                send_email('کد فعالسازی', to=user.email, template="email/email.html", context={"code":code})

            context = {
                'forms':forms,
            }
            return HttpResponse(request.POST.get('check'), context)
        else:
            sweetify.error(request, 'لطفا شرابط را قبول کنید')
            return render(request, 'account/register.html')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        forms = LoginForm()
        context = {
            'forms': forms,
        }
        return render(request, 'account/login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        forms = LoginForm(request.POST)
        context = {
            'forms': forms,
        }
        if forms.is_valid():
            email = forms.cleaned_data.get('email')

            password = forms.cleaned_data.get('password')
            user = get_object_or_404(User, email=email)
            if user.is_active:
                if user.check_password(password):
                    login(request, user)
                    sweetify.success(request, 'با موفقیت وارد شدید')
                    return redirect(reverse('home'))
                else:
                    sweetify.error(request, 'رمز عبور یا حساب کاربری نامعتبر می باشد')
                    return render(request, 'account/login.html', context)
            else:
                sweetify.error(request, 'لطفا حساب کاربریتان را فعال نمائید')
                return render(request, 'account/login.html', context)

@login_required
def log_out(request):
    logout(request)
    sweetify.success(request, 'با موفقیت خارج شدید')
    return redirect(reverse('home'))


def activate_email(request, code):
    user = get_object_or_404(User, activated_code=code)
    if user.is_active == False:
        user.is_active = True
        user.activated_code = create_activation_code()
        user.save()
        return redirect(reverse('home'))

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user = request.user

        context = {
            'user': user,
        }
        return render(request, 'account/profile/main.html', context)


@method_decorator(login_required, name='dispatch')
class ChangePasswordRequest(View):
    def get(self, request):
        user = request.user
        subject = 'تغییر رمز عبور'
        template = 'email/change_pass.html'

        data = user.activated_code
        context = {
            'data': data
        }
        user.activated_code = create_activation_code()
        send_email(subject=subject, to=user.email, context=context, template=template)
        sweetify.success(request, 'ایمیل با موفقیت ارسال شد')
        return redirect(reverse('profile'))



@method_decorator(login_required, name='dispatch')
@method_decorator(require_GET, name='dispatch')
class ChangePassword(View):
    def get(self, request, data):
        user = request.user
        if user.activated_code == data:
            form = ChangePasswordForm()
            context = {
                'form': form,
            }
            return render(request, 'account/profile/change_password.html', context)
        else:
            sweetify.error(request, 'لینک ورود به تغییر رمز عبور نا معتبر میباشد')
            return redirect(reverse('home'))


@method_decorator(login_required, name='dispatch')
# @method_decorator(require_POST, name='dispatch')
class ChangePasswordPost(View):
    def get(self, request):

        return redirect(reverse('profile'))

    def post(self, request):
        form = ChangePasswordForm(request.POST)

        user = request.user
        if form.is_valid():
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            sweetify.success(request, 'با موفقیت رمز عبور تغییر یافت')
            logout(request)
            return redirect(reverse('login'))
        else:
            context = {
                'form': form,
            }
            sweetify.error(request, 'مشکلی بوجود آمده است')
            return render(request, 'account/profile/change_password.html', context)
def avatar_component(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'account/profile/avatar_component.html', context)


@method_decorator(login_required, name='dispatch')
class ListOrderView(ListView):
    model = Order
    template_name = 'account/profile/list_order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        qs = super(ListOrderView, self).get_queryset()
        qs = qs.filter(user=self.request.user, is_paid=True)
        return qs


@method_decorator(login_required, name='dispatch')
class OrderDetailView(ListView):
    model = OrderDetail
    template_name = 'account/profile/detail_order.html'
    context_object_name = 'order_details'

    def get_queryset(self):
        print(self.request.resolver_match.view_name)
        qs = super(OrderDetailView, self).get_queryset()
        qs = qs.filter(order__id=self.kwargs.get('pk'), order__user=self.request.user, order__is_paid=True)
        return qs
