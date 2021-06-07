from django.db import models
from customer.models import *
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=200)
    categoryDescription = models.TextField()
    categoryImage = models.ImageField(upload_to='static/images', default='static/images/3lions.jpeg')

    def __str__(self):
        return self.categoryname


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    productname = models.CharField(max_length=200)
    productcost = models.IntegerField()
    productimage = models.ImageField()
    productquantity = models.IntegerField()


class CustomerProduct(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    customer_product = models.ForeignKey(CustomerProduct, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField()
    delivery_status = models.IntegerField()