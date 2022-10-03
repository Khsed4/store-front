from ast import Index
from dataclasses import fields
from email.policy import default
from enum import unique
from turtle import title
from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()
class Collection(models.Model):
    title = models.CharField(max_length = 255)
    feature_product = models.ForeignKey('Product',on_delete = models.SET_NULL, null = True, related_name = '+')
    

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    
class Product(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(default = '_')
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
    class Meta:
        db_table = 'db_products_changed'
        # indexes = [
        #     models.Index = (fields=['title','unit_price'])
        #     ]
        
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_SILVER, 'silver'),
        (MEMBERSHIP_BRONZE, 'Bronze'),
    ]
    giver_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICE, default=MEMBERSHIP_SILVER)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETED = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES =[(PAYMENT_STATUS_PENDING,'Pending'),(PAYMENT_STATUS_FAILED,'Failed'),(PAYMENT_STATUS_COMPLETED,'Completed')]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_satus = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default= PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)


class Address(models.Model):
    street  = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    # one to one relationship
    # customer = models.OneToOneField(Customer, on_delete = models.CASCADE,primary_key = True)
    #  one to many relationship
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits= 6, decimal_places = 2)

class CartItem (models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quntity =  models.PositiveBigIntegerField()

