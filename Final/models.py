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
    phonenumber = models.CharField(max_length=200) #was an integer field, might need to change back
    email = models.CharField(max_length=30)

    def UsertoStr(self):
        return "User: " + self.username + " " + self.password + " " + self.permissions + " " \
               + self.address + " " + self.phonenumber + " " + self.email

#Todo - Figure out how to represent the LabList with the Course Model
#class Lab(models.Model):
#    labId = models.CharField(max_length = 50)
#    LabStartTime = models.CharField(max_length = 50)
#    LabEndTime = models.CharField(max_length = 50)

#    def LabtoStr(self):
#    return "LabtoStr: " + self.LabId + self.LabStartTime + self.LabEndTime

class Course(models.Model):
    courseId = models.CharField(max_length = 50)
    startTime = models.CharField(max_length = 50)
    endTime = models.CharField(max_length = 50)
    #LabList = models.ManyToManyField(Lab)

    def CoursetoStr(self):
        return "CoursetoStr: " + self.courseId + self.startTime + self.endTime + self.LabList



