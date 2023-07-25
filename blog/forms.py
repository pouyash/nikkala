from django import forms

from blog.models import CommentBlog


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = CommentBlog
        fields = ['email', 'name', 'comment']

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل',
                'class': 'form-control form-control-lg'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'نام',
                'class': 'form-control form-control-lg'
            }),
            'comment': forms.Textarea(attrs={
                'placeholder': 'متن نظر شما',
                'class': 'form-control',
                'rows': 10,
            })
        }

