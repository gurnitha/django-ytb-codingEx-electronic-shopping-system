# apps/store/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.store.models import Product, Category 

# Create your views here.


# Views: ProductList
def ProductList(request):
	# Product list
	product_list = Product.objects.filter(status='Publish')
	# Categories
	categories = Category.objects.all()
	context = {
		'product_list_objects': product_list,
		'category_objects': categories,
	}
	return render(request, 'store/product-list.html', context)
