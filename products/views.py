from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def get_products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products':products})
    
def view_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/view_product.html', {'product':product})