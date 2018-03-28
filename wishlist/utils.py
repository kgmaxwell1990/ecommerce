from django.shortcuts import get_object_or_404
from products.models import Product


def get_wishlist_items(wishlist):
    
    wishlist_items = []
    for item in wishlist:
        this_product = get_object_or_404(Product, pk=item)
        this_item = {
            "id": this_product.id,
            "image": this_product.image,
            "name": this_product.name,
            "price": this_product.price,
            "stars": this_product.stars,
            "average_rating": this_product.average_rating,
            "needs_half_star": this_product.needs_half_star,
        }
        wishlist_items.append(this_item)
        
    return {'wishlist_items':wishlist_items}