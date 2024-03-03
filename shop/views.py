from django.shortcuts import render

from books.models import Book
from shop.models import Cart, CartItem


def shop_list(request):
    books = Book.objects.order_by('-datetime_created')

    context = {
        'books': books
    }

    return render(request, 'shop/shop.html', context)


def shoping(request):

    cart = Cart.objects.get(customer=request.user)
    cart = cart.cart_item.all()

    price_total = 0
    for cart_item in cart:
        price_total += cart_item.result_price

    context = {
        'cart': cart,
        'total_price': price_total,
    }

    return render(request, 'shop/shoping.html', context=context)
