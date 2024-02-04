import os

from django.shortcuts import render, redirect, get_object_or_404

from .models import Book


def books(request):
    book = Book.objects.all()

    context = {
        'books': book,
    }
    return render(request, 'books/books.html', context)


def create(request):
    if request.method == 'POST':
        pass
    return render(request, 'books/create_edit.html',)


def edit(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        print(request.POST)

    context = {
        'book': book
    }
    return render(request, 'books/create_edit.html', context)


def detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    comments = book.comment_book.all()
    context = {
        'book': book,
        'comments': comments
    }
    return render(request, 'books/book.html', context)


def delete(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        if request.POST['status'] == 'yes':
            if book.photo:
                os.remove(book.photo.path)
            book.delete()
            return redirect('home')
    context = {
        'book': book.title
    }
    return render(request, 'books/delete.html', context)
