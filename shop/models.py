from django.db import models
from django.contrib.auth import get_user_model

from books.models import Book


class Cart(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='cart')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    product = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='cart_item')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    unit_price = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    result_price = models.PositiveIntegerField()

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.number} of {self.product}'

    def save(self, *args, **kwargs):
        self.unit_price = self.product.price
        self.result_price = self.unit_price * self.number
        return super(CartItem, self).save(*args, **kwargs)


