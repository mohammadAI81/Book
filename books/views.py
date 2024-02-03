from django.shortcuts import render, redirect, get_object_or_404

from .models import Book, Comment


def books(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'books/books.html', context)


def create(request):
    if request.method == 'POST':
        pass
    return render(request, 'books/create_edit.html',)


def edit(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        pass

    context = {
        'book': book
    }
    return render(request, 'books/create_edit.html', context)


def detail(request, pk):
    book = Book.objects.get(id=pk)

    context = {
        'book': book
    }
    return render(request, 'books/book.html', context)


def delete(request, pk):
    book = Book.objects.get(id=pk)
    context = {
        'book': book.title
    }
    return render(request, 'books/', context)
