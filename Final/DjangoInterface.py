from Final.models import *
from django.db import models
from WorkingModels.CourseInfo import CourseInfo

class DjangoInterface():

    #Getters
    def login_username(self, username):
        user = User.objects.get(username=username)
        if user is None:
            return "User invalid"
        return user

    def login_password(self, passwordP):
        retPass = User.objects.get(password = passwordP)
        if retPass is None:
            return "password invalid"
        return retPass.password

    def user_permissions(self, permissionP):
        retPermissions = User.objects.get(permissions = permissionP)
        if retPermissions.permissions is None:
            return "address DNE"
        return retPermissions.permissions

    def user_address(self, addressP):
        retAddress = User.objects.get(address = addressP)
        if retAddress.address is None:
            return "address DNE"
        return retAddress.address

    def user_email(self, emailP):
        retEmail = User.objects.get(email = emailP)
        if retEmail.email is None:
            return "email DNE"
        return retEmail.email

    def user_phoneNum(self, phoneNumP):
        retPhoneNum = User.objects.get(phonenumber = phoneNumP)
        if retPhoneNum.phonenumber is None:
            return "Phone number DNE"
        return retPhoneNum.phonenumber

    #Course functions
    def course_ID(self, courseIDP):
        retID = Course.objects.get(courseId=courseIDP)
        if retID.courseId is None:
            return "Course ID DNE"
        return retID.courseId

    def course_startTime(self, startTimeP):
        retStartTime = Course.objects.get(startTime = startTimeP)
        if retStartTime is None:
            return "Start time DNE"
        return retStartTime.startTime

    def course_endTime(self, endTimeP):
        retEndTime = Course.objects.get(endTime = endTimeP)
        if retEndTime is None:
            return "End time DNE"
        return retEndTime.endTime

    def getCourse(self, courseIDP):
        retCourse = Course.objects.get(courseId=courseIDP)
        return retCourse

    def getLab(self, labNumberP):
        retLab = Lab.objects.get(labNumber=labNumberP)
        return retLab

    # Fix
    # def course_studentsInCourse(self, courseIDP):
    #     c = Course.objects.get(courseId=courseIDP)
    #     ListofStudents = None
    #     if c.studentsInCourse.count() > 0:
    #         for i in range(1, c.studentsInCourse.count()):
    #             u = c.studentsInCourse.get(i)
    #             ListofStudents += c.studentsInCourse.get


    def get_all_courses(self):
        all_courses = Course.objects.all()
        List = []
        for course in all_courses:
            List.append(CourseInfo(course_name=course.courseId,start_time=course.startTime, end_time=course.endTime, tas_per_course= course.TAsInCourse.all(), students_per_course=course.studentsInCourse.all()))

        return List

    def get_all_classes_by_instructor(self, instructor_name):
        all_courses_with_this_instructor = Course.objects.filter(instructor=instructor_name)
        course_list = []
        for course in all_courses_with_this_instructor:
            course_list.append(
                CourseInfo(course_name=course.courseId, start_time=course.startTime, end_time=course.endTime,
                           tas_per_course=course.TAsInCourse.all(), students_per_course=course.studentsInCourse.all()))
        return course_list

    def get_all_users_in_system(self):
        return User.objects.get()

    # Setters
    def create_user(self, UsernameP, PasswordP, PermissionsP, AddressP, PhoneNumberP, EmailP):
        U = User.objects.create(username=UsernameP, password=PasswordP, permissions=PermissionsP,
                                address=AddressP, phonenumber=PhoneNumberP, email=EmailP)
        U.save()

    def delete_user(self, UserNameP):
        U = User.objects.get(username=UserNameP)
        if U is not None:
            U.delete()
        else:
            print("Error: Invalid user, cannot delete")

    def update_user(self, UsernameP, FieldtoChange, UpdatedInfo):
        u = User.objects.get(username=UsernameP)
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
            else:
                return "Tried to change illegal field"
        u.save()

    def create_course(self, instructorP, courseIDP, startTimeP, endTimeP):
        c = Course.objects.create(instructor=instructorP, courseId=courseIDP, startTime=startTimeP, endTime=endTimeP)
        c.save()

    def delete_course(self, courseIDP):
        c = Course.objects.get(courseId=courseIDP)
        if c is not None:
            c.delete()
        else:
            print("Error: Invalid course, cannot delete")

    def add_user_to_course(self, courseIDP, usernameP):
        c = Course.objects.get(courseId=courseIDP)
        # Probably do a for loop for a list of students instead of a single one at a time, but fuck it we're doing it later.
        u = User.objects.get(username=usernameP)
        c.studentsInCourse.add(u)
        c.save()
        print(c.studentsInCourse.all())

    def add_TA_to_course(self, courseIDP, TAnameP):
        c = Course.objects.get(courseId=courseIDP)
        u = User.objects.get(username=TAnameP)
        c.TAsInCourse.add(u)
        c.save()
        print(c.TAsInCourse.all())

    def update_course(self, CourseIDP, FieldtoChange, UpdatedInfo):
        c = Course.objects.get(courseId=CourseIDP)
        # figure out how to get switch statements working dumbass
        if c is not None:
            if FieldtoChange == "courseId":
                c.courseId = UpdatedInfo
            elif FieldtoChange == "startTime":
                c.startTime = UpdatedInfo
            elif FieldtoChange == "endTime":
                c.endTime = UpdatedInfo
            else:
                return "Tried to change illegal field"
        c.save()

    def create_lab(self, labnumberP, TAnameP, startTimeP, endTimeP):
        # c = Course.objects.get(courseId=courseIDP) ##Might need to change later, dependent on if we want a distinct call for adding a course to a lab section or if we want to do it upon creation.
        # if c is not None:
        l = Lab.objects.create(labNumber=labnumberP, TA=TAnameP, startTime=startTimeP, endTime=endTimeP)
        l.save()
        #print("Error: Trying to create a lab section with incorrect parent course in DjangoInterface.")

    def delete_lab(self, labnumberP):
        l = Lab.objects.get(labNumber=labnumberP)
        if l is not None:
            l.delete()
        else:
            print("Error: Invalid lab, cannot delete")

    def add_student_to_lab (self, labP, studentP):
        labP.studentsInLab.add(studentP)
        studentP.save()
        print(labP.studentsInLab.all()) #remove later

    def add_lab_section_to_course(self, labP, courseIDP):
        labP.ParentCourse = courseIDP
        labP.save()