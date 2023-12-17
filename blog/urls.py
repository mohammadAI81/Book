from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs, name='list_blog'),
    path('create/', views.create, name='create_blog'),
    path('detail/<int:num>', views.detail, name='detail_blog'),
    path('edit/<str:name>/', views.edit, name='edit_blog'),
    path('delete/<str:name>/', views.delete, name='delete_blog'),
]