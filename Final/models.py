from django.db import models


# Create your models here.
class MyModel(models.Model):
    fieldOne = models.CharField(max_length=20)
    fieldTwo = models.IntegerField(default=0)


class User(models.Model):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    permissions = models.CharField(max_length=20)
    # pa = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phonenumber = models.IntegerField(default=0)
    email = models.CharField(max_length=30)

    # Wrong(?)
    def usertostr(self):
        return "UsertoStr: " + self.username


class Lab(models.Model):

    labId = models.CharField(max_length=50)
    LabStartTime = models.CharField(max_length=50)
    LabEndTime = models.CharField(max_length=50)


class Course(models.Model):

    courseId = models.CharField(max_length=50)
    startTime = models.CharField(max_length=50)
    endTime = models.CharField(max_length=50)
    LabList = models.ManyToManyField(Lab)
