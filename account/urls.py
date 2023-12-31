from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('activate/<code>/', views.activate_email, name='activate_email'),
    path('logout/', views.log_out, name='logout'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('change_password_request/', views.ChangePasswordRequest.as_view(), name='change_password_request'),
    path('change_password/<data>', views.ChangePassword.as_view(), name='change_password'),
    path('change_password/', views.ChangePasswordPost.as_view(), name='change_password_post'),
    path('orders/', views.ListOrderView.as_view(), name='user_orders'),
    path('orders_detail/<pk>', views.OrderDetailView.as_view(), name='user_order_detail'),
    path('product_favorites/', views.ListFavoriteView.as_view(), name='product_favorites_in_account'),
    path('blogs/', views.BlogsAccountView.as_view(), name='blogs_in_account'),
    path('blog_create/', views.BlogCreateAccountView.as_view(), name='blogs_create_in_account'),
    path('blog_edit/<pk>/', views.BlogEditAccountView.as_view(), name='blogs_edit_in_account'),
    path('blog_delete/<pk>/', views.BlogDeleteAccountView.as_view(), name='blogs_delete_in_account'),

]
