from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog


class RegisterForm(forms.Form):
    email = forms.CharField(label='ایمیل',widget=forms.EmailInput({
        'class': 'form-control form-control-lg signup-login-input'
    }))
    name = forms.CharField(label='نام کاربری',widget=forms.TextInput({
        'class': 'form-control form-control-lg signup-login-input'
    }))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput({
        'class': 'form-control form-control-lg signup-login-input'
    }))
    confirm_password = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput({
        'class': 'form-control form-control-lg signup-login-input'
    }))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('رمز عبور و تکرار رمز عبور متفاوت است')


class LoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg signup-login-input'
    }))

    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput({
        'class': 'form-control form-control-lg signup-login-input'
    }))



class ChangePasswordForm(forms.Form):

    password = forms.CharField(label='رمز عبور جدید', widget=forms.PasswordInput(attrs={
        'label': 'رمز عبور',
        'class': 'form-control form-control-lg signup-login-input',
        'placeholder': 'رمز عبور جدید'
    }))

    confirm_password = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={
        'label': 'تکرار رمز عبور',
        'class': 'form-control form-control-lg signup-login-input',
        'placeholder': 'تکرار رمز عبور'
    }))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('رمز عبور جدید با تکرار رمز عبور متفاوت است.')


class BlogsForm(forms.ModelForm):
    description = CKEditorUploadingWidget()
    class Meta:
        model = Blog
        fields = ['title', 'image', 'short_description', 'description', 'is_active', 'category', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان وبلاگ',
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'توضیحات مختصر',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',

            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
            'image': forms.FileInput()

        }

        labels = {
            'title': 'عنوان وبلاگ',
            'description': 'متن وبلاگ',
        }
