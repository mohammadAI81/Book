from django.urls import path

from . import views

urlpatterns = [
    path('Shop/', views.shop_list, name='shop-list'),
    path('Shoping/', views.shoping, name='shoping'),
]
