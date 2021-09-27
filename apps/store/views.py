# apps/store/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.store.models import Product

# Create your views here.


# Views: ProductList
def ProductList(request):
	product_list = Product.objects.filter(status='Publish')
	context = {
		'product_list_objects': product_list,
	}
	return render(request, 'store/product-list.html', context)
