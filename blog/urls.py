from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<cat>/', views.BlogsView.as_view(), name='blogs'),
    path('blog/<slug>', views.BlogDetailView.as_view(), name='blog_detail'),
]