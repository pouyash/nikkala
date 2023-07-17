from django.urls import path

from order import views

urlpatterns = [
    path('add_to_card/<slug>/', views.AddToCardView.as_view(), name='add_to_card'),
    path('card', views.CardView.as_view(), name='card'),

    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]