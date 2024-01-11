from django.shortcuts import render, redirect
from django.views import View
from store.models import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart', {}).keys())   # Use {} as a default value if 'cart' is not present
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})
    
