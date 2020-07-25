from django.shortcuts import render

# Create your views here.
def products(request):
    return render(request, 'shop/shop.html')

def product(request):
    return render(request, 'shop/single-shop.html')
