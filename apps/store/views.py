# apps/store/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.store.models import (
	Product, 
	Category, 
	FilterPrice,
	) 

# Create your views here.


# Views: ProductList
def ProductList(request):

	# Product list
	product_list = Product.objects.filter(status='Publish')

	# Categories
	categories = Category.objects.all()

	# FilterPrice
	filter_prices = FilterPrice.objects.all()

	context = {
		'product_list_objects': product_list,
		'category_objects': categories,
		'filter_price_objects': filter_prices,
	}
	return render(request, 'store/product-list.html', context)
