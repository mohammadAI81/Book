from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list_blog'),
    path('create/', views.create, name='create_blog'),
    path('detail/<int:num>/', views.detail, name='detail_blog'),
    path('edit/<int:num>/', views.edit, name='edit_blog'),
    path('delete/<int:num>/', views.delete, name='delete_blog'),
]