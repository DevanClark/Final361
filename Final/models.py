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
    instructor = models.CharField(max_length=50)
    courseId = models.CharField(max_length=50)
    startTime = models.CharField(max_length=50)
    endTime = models.CharField(max_length=50)
    studentsInCourse = models.ManyToManyField(User,  blank=True)


    def CoursetoStr(self):
        return "CoursetoStr: " + self.instructor + self.courseId + self.startTime + self.endTime + self.LabList

#Intermediate table, see https://stackoverflow.com/questions/48992233/django-manytomanyfield-initializes-with-all-objects-by-default
#class Students(models.Model):
#    users = models.ForeignKey(User, on_delete=models.CASCADE)
#    studentsInCourse = models.ForeignKey(Course, on_delete=models.CASCADE)