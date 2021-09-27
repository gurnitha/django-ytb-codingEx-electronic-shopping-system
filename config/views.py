# config/views.py

# Django modules
from django.shortcuts import render, redirect

# Locals
from apps.store.models import Product  

# Create your views here.

# Base template
def BASE(request):
	return render(request, 'base/base.html')


# Views: HomePage
def HomePage(request):
	# products = Product.objects.all()
	products = Product.objects.filter(status='Publish')
	context = {
		'product_objects':products,
	}
	return render(request, 'base/index.html', context)
