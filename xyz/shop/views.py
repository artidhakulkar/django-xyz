from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    product = Product.objects.all()
    print(product)
    n = len(product)
    nSlide = n//4 + ceil((n/4) + (n//4))
    params= {'no_of_slides': nSlide, 'range': (1, nSlide), 'product': product}
    return render(request, 'shop/index.html', params)

def about(request):
   return render(request, 'shop/about.html')

def contact(request):

    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/productview.html')

def checkout(request):
    return render(request, 'shop/checkout.html')