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
    instructor = models.CharField(max_length=50, null=True)
    courseId = models.CharField(max_length=50)
    startTime = models.CharField(max_length=50)
    endTime = models.CharField(max_length=50)
    studentsInCourse = models.ManyToManyField(User,  blank=True, related_name='students')
    TAsInCourse = models.ManyToManyField(User, blank=True, related_name='TAs')

    def CoursetoStr(self):
        return "CoursetoStr: " + self.instructor + self.courseId + self.startTime + self.endTime \
               + self.studentsInCourse.all(), self.TAsInCourse.all()

class Lab(models.Model):
    labNumber = models.CharField(max_length=50)
    TA = models.CharField(max_length=50)
    studentsInLab = models.ManyToManyField(User, blank=True, related_name='studentsInThisRelNameLab')
    startTime = models.CharField(max_length=50)
    endTime = models.CharField(max_length=50)
    ParentCourse = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)

    def LabtoStr(self):
        return "Lab: " + self.labNumber + " " + self.TA + " " + \
               self.startTime + " " + self.endTime + " " + self.ParentCourse.__str__() #Might need to print studentsInLab separately


#Intermediate table, see https://stackoverflow.com/questions/48992233/django-manytomanyfield-initializes-with-all-objects-by-default
#class Students(models.Model):
#    users = models.ForeignKey(User, on_delete=models.CASCADE)
#    studentsInCourse = models.ForeignKey(Course, on_delete=models.CASCADE)