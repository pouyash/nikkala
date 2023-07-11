from xml.dom import ValidationErr

from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpRequest

from contact_us.models import ContactUs


class ContactUsForms(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"
        required = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'عنوان',
                'class': 'form-control form-control-lg',
            }),
            'fullname': forms.TextInput(attrs={
                'placeholder': 'نام و نام خانوادگی',
                'class': 'form-control form-control-lg',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل',
                'class': 'form-control form-control-lg',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'تلفن',
                'class': 'form-control form-control-lg',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'متن پیغام شما',
                'class': 'form-control',
                'rows': 5,
            }),
        }

        labels = {
            'title': 'عنوان',
            'email': 'ایمیل',
            'fullname': 'نام و نام خانوادگی',
            'message': 'متن پیغام',
            'phone': 'شماه موبایل',
        }

    def clean_phone(self):
        if len(self.cleaned_data.get('phone')) != 11:
            raise ValidationError("تعداد باید 11 عدد باشد")
        else:
            return self.cleaned_data.get('phone')


