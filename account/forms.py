from django import forms
from django.core.exceptions import ValidationError


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