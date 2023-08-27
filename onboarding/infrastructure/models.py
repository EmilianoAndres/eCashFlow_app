from django.db import models


class CustomerPersistence(models.Model):
    class Meta:
        db_table = "customer"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()


class OrderPersistence(models.Model):
    class Meta:
        db_table = "order"
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        CustomerPersistence, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
