# apps/store/urls.py

# Django modules
from django.urls import path

# Locals
from apps.store.views import ProductList

app_name = 'store'

urlpatterns = [
    path('products/', ProductList, name='product_list'),  
]
