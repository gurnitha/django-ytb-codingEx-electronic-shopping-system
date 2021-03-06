# apps/store/models.py

# Django modulese
from django.db import models
from django.utils import timezone

# Create your models here.

# Model:Category
class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


# Model:Brand
class Brand(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


# Model:Color
class Color(models.Model):
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=50)

	def __str__(self):
		return self.name


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
	)
	price = models.CharField(choices=FILTER_PRICE, max_length=60)

	def __str__(self):
		return self.price


# Model:Product
class Product(models.Model):

	CONDITION = (('New','New'),('Old','Old'))
	STOCK =  (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
	STATUS =  (('Publish','Publish'),('Draft','Draft'))

	unique_id = models.CharField(unique=True,max_length=200,null=True,blank=True)
	image = models.ImageField(upload_to='media/product/images')
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	condition = models.CharField(choices=CONDITION,max_length=100, default='New')
	information = models.TextField()
	description = models.TextField()
	stock = models.CharField(choices=STOCK, max_length=50, default='In Stock')
	status = models.CharField(choices=STATUS, max_length=50, default='Publish')
	created_date = models.DateTimeField(default=timezone.now)
	updated_date = models.DateTimeField(auto_now=True)

	# Adding relationship with
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
	color = models.ForeignKey(Color,on_delete=models.CASCADE)
	filter_price = models.ForeignKey(FilterPrice,on_delete=models.CASCADE)

	# Save the created unique_id
	def save(self, *args, **kwargs):
		if self.unique_id is None and self.created_date and self.id:
			self.unique_id = self.created_date.strftime('75%Y%m%d23' + str(self.id))
		return super().save(*args,**kwargs)

	def __str__(self):
		return self.name


# Model:Image
class Images(models.Model):
	image = models.ImageField(upload_to='media/product/images')
	product = models.ForeignKey(Product,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Images'

	# def __str__(self):
	# 	return self.product


# Model:Tag
class Tag(models.Model):
	name = models.CharField(max_length=200)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return self.name
