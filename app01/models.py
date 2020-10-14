from django.db import models

# Create your models here.


class TT(models.Model):
    title = models.CharField(max_length=32)

class Product(models.Model):
    productname = models.CharField(max_length=32,unique=True)
    productkey = models.CharField(max_length=32,unique=True)
    productsecret = models.CharField(max_length=32)

class Device(models.Model):
    devicename = models.CharField(max_length=32)
    devicesecret = models.CharField(max_length=32)
    productname = models.ForeignKey('Product',to_field='productname',on_delete=models.CASCADE)

class Test2(models.Model):
    device_name = models.CharField(max_length=32)
    event_time = models.IntegerField()
    event_date = models.DateField()
    product_key = models.ForeignKey('Product',to_field='productkey',on_delete=models.CASCADE)
    CurrentTemperature = models.FloatField()
    CurrentHumidity = models.FloatField()
