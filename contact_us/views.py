import sweetify
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from contact_us.forms import ContactUsForms


class ContactUsView(View):
    def get(self, request):
        forms = ContactUsForms()
        if request.user.is_authenticated:
            forms = ContactUsForms(initial={'email':request.user.email})
        context = {
            'forms': forms
        }

        return render(request, 'contact_us/contact.html', context)

    def post(self, request:HttpRequest):
        forms = ContactUsForms(request.POST)

        if forms.is_valid():
            obj = forms.save(commit=False)
            if request.user.is_authenticated:
                obj.email = request.user.email
            obj.save()
            sweetify.success(request, 'با موفقیت پیغام شما ارسال شد. باتشکر از مشارکتتان !')
            return redirect(reverse('home'))

        sweetify.error(request, 'مشکلی بوجود آمده است')
        context = {
            'forms': forms
        }
        return render(request, 'contact_us/contact.html', context)