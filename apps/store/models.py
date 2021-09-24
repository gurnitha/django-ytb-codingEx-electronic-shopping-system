# apps/store/models.py

# Django modulese
from django.db import models

# Create your models here.

# Model:Category
class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Categories'

# Model:Brand
class Brand(models.Model):
	name = models.CharField(max_length=200)


# Model:Color
class Color(models.Model):
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=50)


# Model:Filter_Price
class FilterPrice(models.Model):
	FILTER_PRICE = (
		('1 TO 50','1 TO 50'),
		('50 TO 100','50 TO 100'),
		('100 TO 200','100 TO 200'),
		('200 TO 300','200 TO 300'),
		('300 TO 400','300 TO 400'),
		('400 TO 500','400 TO 500'),
		('500 TO 600','500 TO 600'),
		('600 TO 700','600 TO 700'),
		('700 TO 800','700 TO 800'),
		('900 TO 1000','900 TO 1000'),
		('',''),
	)
	price = models.CharField(choices=FILTER_PRICE, max_length=60)
