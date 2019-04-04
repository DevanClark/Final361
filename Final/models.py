from django.db import models


# Create your models here.
class MyModel(models.Model):
    fieldOne = models.CharField(max_length=20)
    fieldTwo = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    permissions = models.CharField(max_length=20)
    pa = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phonenumber = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
