from urllib import request

from django.contrib.auth.models import User
from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

from mainsite.models import addProduct
# Create your models here.

class order(models.Model):
    user = UserForeignKey(auto_user_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "order"
        verbose_name_plural = "orders"
    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(addProduct,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    def __str__(self):
        return '{}'.format(self.id)
    def get_cost(self):
        return self.price * self.quantity













































































