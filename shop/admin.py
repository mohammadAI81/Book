from django.contrib import admin

from .models import CartItem, Cart


class CartItemOfCart(admin.StackedInline):
    model = CartItem
    fields = ['product', 'number']
    extra = 2


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'unit_price', 'number', )
    list_editable = ('number', 'product', )
    list_per_page = 25


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', )
    inlines = [
        CartItemOfCart,
    ]

