from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_blog, name='list_blog'),
    path('create/', views.create, name='create_blog'),
    path('edit/<str:name>/', views.edit, name='edit_blog'),
    path('delete/<str:name>/', views.delete, name='delete_blog'),
]