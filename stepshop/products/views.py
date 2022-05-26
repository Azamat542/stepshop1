from django.shortcuts import render


def product(request):
    return render(request, 'single-product.html')


def products(request):
    return render(request, 'products.html')
