from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from books.models import Book
from cart.models import Cart, CartItem


def shop_list(request):
    books = Book.objects.select_related('author').order_by('-datetime_created')

    context = {
        'books': books
    }

    return render(request, 'shop/shop.html', context)


@login_required(login_url='/account/login/')
def shopping(request):

    cart = False
    price_total = None
    if Cart.objects.exists():
        cart = Cart.objects.get(customer=request.user)
        cart = cart.cart_item.select_related('product')

        if cart.count() <= 0:
            return

        price_total = 0
        for cart_item in cart:
            price_total += cart_item.result_price

    context = {
        'cart': cart,
        'total_price': price_total,
    }

    return render(request, 'shop/shoping.html', context=context)
