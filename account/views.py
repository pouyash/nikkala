import sweetify
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from utils.functions import create_activation_code
# Create your views here.
from django.urls import reverse
from django.views import View

from account.forms import RegisterForm, LoginForm
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
                sweetify.error(request, 'لطفا حساب کاربریتان را فعال نمائید')
                return render(request, 'account/login.html', context)


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










