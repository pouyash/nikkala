from django.urls import path

from product import views

urlpatterns = [
    path('<search>/', views.ProductsView.as_view(), name='products'),
    path('order/<order>/', views.ProductsView.as_view(), name='products_order'),
    path('product/<slug>', views.ProductDetailView.as_view(), name='product'),
    path('product/add_to_favorite/<id>', views.add_product_to_favorite, name='product_add_to_favorite'),
]