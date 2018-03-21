from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from products.models import Product

# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    
    cart_items = []
    complete_total = 0
    for item_id, item_quantity in cart.items():
        this_product = get_object_or_404(Product, pk=item_id)
        this_item = {
            "image": this_product.image,
            "name": this_product.name,
            "quantity": item_quantity,
            "price": this_product.price,
            "item_total": this_product.price * item_quantity,
        }
        cart_items.append(this_item)
        complete_total += this_product.price * item_quantity
    
    
    return render(request, "cart/view_cart.html", {'cart_items': cart_items, 'complete_total': complete_total})


def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart   

    return redirect('home')
    
    