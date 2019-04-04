from Final.models import *

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
            return "address invalid"
        return retPermissions

    def user_address(self, addressP):
        retAddress = User.objects.get(address = addressP)
        if retAddress is None:
            return "address invalid"
        return retAddress

    def user_email(self, emailP):
        retEmail = User.objects.get(email = emailP)
        if retEmail is None:
            return "email invalid"
        return retEmail

    def user_phoneNum(self, phoneNumP):
        retPhoneNum = User.objects.get(phonenumber = phoneNumP)
        if retPhoneNum is None:
            return "Phone number invalid"
        return retPhoneNum

    #Course functions
    def course_ID(self, courseIDP):
        retID = User.objects.get(courseId = courseIDP)
        if retID is None:
            return "Course ID invalid"
        return retID

    def course_startTime(self, startTimeP):
        retStartTime = User.objects.get(startTime = startTimeP)
        if retStartTime is None:
            return "Start time invalid"
        return retStartTime

    def course_endTime(self, endTimeP):
        retEndTime = User.objects.get(endTime = endTimeP)
        if retEndTime is None:
            return "End time invalid"
        return retEndTime

    def course_labList(self, LabListP):
        retLabList = User.objects.get(LabList = LabListP)
        if retLabList is None or retLabList is not isinstance(retLabList, list):
            return "Lab List is invalid"
        return retLabList
