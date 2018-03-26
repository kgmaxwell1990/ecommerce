from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages, auth
from django.conf import settings
from .forms import MakePaymentForm, OrderForm
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from products.models import Product
from cart.utils import get_cart_items_and_total
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def get_checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        order = order_form.save(commit=False)
        order.date = timezone.now()
        order.save()
        
        cart = request.session.get('cart', {})
        for id, quantity in cart.items():
            product = get_object_or_404(Product, pk = id)
            order_line_item = OrderLineItem(
                order = order,
                product = product,
                quantity = quantity
            )
            order_line_item.save()
        
        # take payment
        payment_form = MakePaymentForm(request.POST)
        if payment_form.is_valid():
            total = get_cart_items_and_total(cart)['total']
            total_in_cent = int(total * 100)
            try:
                customer = stripe.Charge.create(
                   amount= total_in_cent,
                   currency="EUR",
                   description="Dummy Transaction",
                   card=payment_form.cleaned_data['stripe_id'],
               )
                if customer.paid:
                   messages.success(request, "You have successfully paid")
            except stripe.error.CardError:
               messages.error(request, "Your card was declined!")


            
        
        # clear the cart
        del request.session['cart']
        messages.success(request, "Thanks for your order!")
        return redirect('home')
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'publishable':settings.STRIPE_PUBLISHABLE_KEY, 'order_form':order_form, 'payment_form':payment_form}
        cart_items_and_total = get_cart_items_and_total(request.session.get('cart', {}))
        context.update(cart_items_and_total)

        return render(request, "checkout/checkout.html", context)
    