from django.db import models
from abc import ABC, abstractmethod

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    # ... other fields ...


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # ... other fields ...
