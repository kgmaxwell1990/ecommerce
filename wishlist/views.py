from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .utils import get_wishlist_items
from products.models import Product

# Create your views here.
def view_wishlist(request):
    wishlist = request.session.get('wishlist', {})
    if not wishlist:
        return render(request, "wishlist/empty_wishlist.html")
    context = get_wishlist_items(wishlist)
    return render(request, "wishlist/wishlist.html", context)
    
    
def add_to_wishlist(request):
    id = request.POST['id']
    quantity = 1
    wishlist = request.session.get('wishlist', {})
    wishlist[id] = wishlist.get(id, 0) + quantity
    request.session['wishlist'] = wishlist
    messages.success(request, "You added to your wishlist!")
    print(wishlist)
    return redirect(request.GET.get('next', 'home'))
    
    
def remove_wishlist_item(request, id):
    wishlist = request.session.get('wishlist', {})
    del wishlist[id]
    request.session['wishlist'] = wishlist
    messages.success(request, "You deleted from your wishlist!")
    return redirect(request.GET.get('next', 'home'))

    
    