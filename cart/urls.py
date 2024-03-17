from django.urls import path

from . import views

urlpatterns = [
    path('Shop/', views.shop_list, name='cart-list'),
    path('Shopping/', views.shopping, name='shopping'),
]
