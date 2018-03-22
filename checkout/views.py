from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages, auth
from .forms import MakePaymentForm, OrderForm
from cart.utils import get_cart_items_and_total

# Create your views here.

def get_checkout(request):
    
    order_form = OrderForm()
    payment_form = MakePaymentForm()
    
    context = {'publishable':0, 'order_form':order_form, 'payment_form':payment_form}
    
    cart_items_and_total = get_cart_items_and_total(request.session.get('cart', {}))
    context.update(cart_items_and_total)

    return render(request, "checkout/checkout.html", context)
    