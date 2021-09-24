# apps/store/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.store.models import (
	Category,
	Brand,
	Color,
	FilterPrice,
	Product,
	Images)

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(FilterPrice)
admin.site.register(Product)
admin.site.register(Images)