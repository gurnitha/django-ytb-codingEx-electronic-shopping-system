# apps/store/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.store.models import (
	Product, 
	Category, 
	FilterPrice,
	Color,
	Brand,
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

	# Color
	colors = Color.objects.all()

	# Brand
	brands = Brand.objects.all()

	# Products-By-Category
	cat_id 			= request.GET.get('category')
	# Products-By-Price
	filter_price_id = request.GET.get('filter_price')

	if cat_id:
		product_list = Product.objects.filter(category=cat_id, status='Publish')

	elif filter_price_id:
		product_list = Product.objects.filter(filter_price=filter_price_id, status='Publish')

	else:
		product_list = Product.objects.filter(status='Publish')

	# Products-By-Price



	context = {
		'product_list_objects': product_list,
		'category_objects': categories,
		'filter_price_objects': filter_prices,
		'color_objects':colors,
		'brand_objects':brands,
	}
	return render(request, 'store/product-list.html', context)
