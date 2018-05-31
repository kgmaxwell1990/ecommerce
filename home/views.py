from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.utils import timezone
from products.models import Product

# Create your views here.

def get_index(request):
    return render(request, "home/index.html")
    