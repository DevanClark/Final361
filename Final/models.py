from django.db import models


# Create your models here.
class MyModel(models.Model):
    fieldOne = models.CharField(max_length=20)
    fieldTwo = models.IntegerField(default=0)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    permissions = models.CharField(max_length=20)

    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)  # was an integer field, might need to change back
    email = models.CharField(max_length=30)

    def UsertoStr(self):
        return "User: " + self.username + " " + self.password + " " + self.permissions + " " \
               + self.address + " " + self.phonenumber + " " + self.email


class Course(models.Model):
    courseId = models.CharField(max_length=50)
    startTime = models.CharField(max_length=50)
    endTime = models.CharField(max_length=50)

    def CoursetoStr(self):
        return "CoursetoStr: " + self.courseId + self.startTime + self.endTime + self.LabList
