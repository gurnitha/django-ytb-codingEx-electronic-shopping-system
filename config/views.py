# config/views.py

# Django modules
from django.shortcuts import render, redirect

# Create your views here.

# Base template
def BASE(request):
	return render(request, 'base/base.html')


# Views: HomePage
def HomePage(request):
	return render(request, 'base/index.html')
