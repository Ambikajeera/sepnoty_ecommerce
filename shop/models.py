from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending','Pending'), 
        ('Processing','Processing'), 
        ('Shipped','Shipped'), 
        ('Delivered','Delivered'), 
        ('Cancelled','Cancelled')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()
    admin_notes = models.TextField(blank=True, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

