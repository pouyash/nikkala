from django.urls import path

from product import views

urlpatterns = [
    path('<search>/', views.ProductsView.as_view(), name='products'),
    path('order/<order>/', views.ProductsView.as_view(), name='products_order'),
    path('product/<slug>', views.ProductDetailView.as_view(), name='product'),
]