from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import OrderCreateForm
from .models import OrderItem
from . import models
from cart.cart import Cart
from django.forms.widgets import HiddenInput


def order_create(request):
    cart = Cart(request)
    r = request.user
    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])

            cart.clear()
            context = {
                'order': order,
                'r': r
            }
            request.session['order_id'] = order.id

            return redirect(reverse('payment:process'))
            #return render(request, 'created.html', context)

    else:
        form = OrderCreateForm()
    context = {
        'cart': cart,
        'form': form,
        'r': r
    }
    return render(request, 'create.html', context)

