from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages
from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.
def get_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})
    
def view_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product_images = ProductImages.objects.filter(product=id)
    form = ReviewForm()
    wishlist = request.session.get('wishlist', {})
    in_wishlist = id in wishlist
    return render(request, 'products/view_product.html', {'product':product, 'review_form': form, 'product_images':product_images, 'in_wishlist': in_wishlist})
    
def order_lowest(request):
    products = Product.objects.order_by('price')
    return render(request, 'products/products.html', {'products':products})
    
def order_highest(request):
    products = Product.objects.order_by('-price')
    return render(request, 'products/products.html', {'products':products})
    
def order_az(request):
    products = Product.objects.order_by('name')
    return render(request, 'products/products.html', {'products':products})
    
def order_za(request):
    products = Product.objects.order_by('-name')
    return render(request, 'products/products.html', {'products':products})