from django.urls import path

from product import views

urlpatterns = [
    path('<search>/', views.ProductsView.as_view(), name='products'),
    path('product/<slug>', views.ProductDetailView.as_view(), name='product'),
]