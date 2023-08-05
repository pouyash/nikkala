from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<cat>/', views.BlogsView.as_view(), name='blogs'),
    path('blog/<slug>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/comment/like/<comment_id>/', views.blog_comment_like, name='blog_comment_like'),
    path('blog/comment/add_to_favorite/<id>/', views.add_session, name='blog_add_to_favorite'),
]