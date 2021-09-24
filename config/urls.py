# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Locals
from config import views 

urlpatterns = [
    
    # Base views: http://localhost:8000/base/
    path('base/', views.BASE, name='base'),

    # Admin
    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


