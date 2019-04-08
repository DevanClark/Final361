from Final.models import *
from django.db import models

class DjangoInterface():

    #Amin
    def login_username(self, username):
        user = User.objects.get(username=username)
        if user is None:
            return "User invalid"  # remove later
        return user

    # def user_ID(self, IDP):
    #   retID = User.objects.get(ID = IDP)
    #  if retID is None:
    #     return "ID invalid."
    #return retID

    #need a function to add users/courses to database.

    def login_password(self, passwordP):
        retPass = User.objects.get(password = passwordP) #Setting the password field in the model to whatever the parameter is.
        if retPass is None:
            return "password invalid"
        return retPass                                   #Returning the new pass

    def user_permissions(self, permissionP):
        retPermissions = User.objects.get(permissions = permissionP)
        if retPermissions is None:
            return "address DNE"
        return retPermissions

    def user_address(self, addressP):
        retAddress = User.objects.get(address = addressP)
        if retAddress is None:
            return "address DNE"
        return retAddress

    def user_email(self, emailP):
        retEmail = User.objects.get(email = emailP)
        if retEmail is None:
            return "email DNE"
        return retEmail

    def user_phoneNum(self, phoneNumP):
        retPhoneNum = User.objects.get(phonenumber = phoneNumP)
        if retPhoneNum is None:
            return "Phone number DNE"
        return retPhoneNum

    #Course functions
    def course_ID(self, courseIDP):
        retID = User.objects.get(courseId = courseIDP)
        if retID is None:
            return "Course ID DNE"
        return retID

    def course_startTime(self, startTimeP):
        retStartTime = User.objects.get(startTime = startTimeP)
        if retStartTime is None:
            return "Start time DNE"
        return retStartTime

    def course_endTime(self, endTimeP):
        retEndTime = User.objects.get(endTime = endTimeP)
        if retEndTime is None:
            return "End time DNE"
        return retEndTime

    def course_labList(self, LabListP):
        retLabList = User.objects.get(LabList = LabListP)
        if retLabList is None or retLabList is not isinstance(retLabList, list):
            return "Lab List is DNE"
        return retLabList

#Setters
    def create_user(self, UsernameP, PasswordP):
        U = User.objects.create(username=UsernameP, password=PasswordP)

    def delete_user(self, UserNameP):
        U = User.objects.get(username=UserNameP).delete()
        if U is not None:
            U.delete()
        else:
            print("Error: Invalid user, cannot delete")

    def update_user(self, UsernameP, FieldtoChange, UpdatedInfo):
        u = User.objects.get(username=UsernameP)   #Getting the user object based on the Username Passed in (UsernameP)

        #figure out how to get switch statements working dumbass
        if u is not None:
            if FieldtoChange == "username":
                u.username = UpdatedInfo
            elif FieldtoChange == "password":
                u.password = UpdatedInfo
            elif FieldtoChange == "permissions":
                u.permissions = UpdatedInfo
            elif FieldtoChange == "address":
                u.address = UpdatedInfo
            elif FieldtoChange == "phonenumber":
                u.phonenumber = UpdatedInfo
            elif FieldtoChange == "email":
                u.email = UpdatedInfo
        u.save()

    def create_course(self, courseIDP, startTimeP, endTimeP):
        c = Course.objects.create(courseId=courseIDP, startTime=startTimeP, endTime=endTimeP)

    def delete_course(self, courseIDP):
        c = Course.objects.get(courseId=courseIDP)
        if c is not None:
            c.delete()
        else:
            print("Error: Invalid course, cannot delete")

