from django.db import models
from customer.models import *
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
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