# apps/store/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.


# Views: ProductList
def ProductList(request):
	return render(request, 'store/product-list.html')
