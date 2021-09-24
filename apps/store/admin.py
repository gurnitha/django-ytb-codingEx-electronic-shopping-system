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
	Images,
	Tag)


# Class:ImagesTabularInline
class ImagesTabularInline(admin.TabularInline):
	model = Images 


# Class:ImagesTabularInline
class TagTabularInline(admin.TabularInline):
	model = Tag 


# Class:ProductAdmin
class ProductAdmin(admin.ModelAdmin):
	inlines = [ImagesTabularInline,TagTabularInline]

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(FilterPrice)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Tag)