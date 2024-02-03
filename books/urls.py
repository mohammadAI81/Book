from django.urls import path

from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('create/', views.create, name='book_create'),
    path('edit/<int:pk>/', views.edit, name='book_edit'),
    path('delete/<int:pk>', views.delete, name='book_delete'),
    path('detail/<int:pk>/', views.detail, name='book_detail'),
]
