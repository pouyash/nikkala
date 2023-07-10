from django.urls import path

from product import views

urlpatterns = [
    path('<search>/', views.ProductsView.as_view(), name='products'),
]