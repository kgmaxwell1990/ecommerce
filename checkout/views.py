from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages, auth
from .forms import MakePaymentForm, OrderForm
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from products.models import Product

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
        
        del request.session['cart']
        messages.success(request, "Thanks for your order!")
        return redirect('home')
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'publishable':0, 'order_form':order_form, 'payment_form':payment_form}
        cart_items_and_total = get_cart_items_and_total(request.session.get('cart', {}))
        context.update(cart_items_and_total)

        return render(request, "checkout/checkout.html", context)
    