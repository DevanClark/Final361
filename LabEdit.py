from Final.DjangoInterface import DjangoInterface
from Final.models import *

django_interface = DjangoInterface()

class LabEdit:
    def __init__(self):
        self = self

    def create_lab(self, TA, labnumber, starttime, endtime, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1': #can instructors create lab sections?
            return "Illegal permissions to do this action"
        try:
            u = User.objects.get(username=TA)

            if u.permissions[3] != '1':
                return "The user you're trying to assign as a TA does not have TA-level permissions (xxx1)"
        except Exception as e:
            TA = "None"
        try:
            django_interface.getLab(labnumber)
        except Exception as e:
            try:
                django_interface.create_lab(labnumber, TA, starttime, endtime)
            except Exception as e:
                print(e)
                return "Failed to create lab."
            return "Lab successfully added"  # Whatever was written in the acceptance tests
        return "This lab already exists"

    def delete_lab(self, labToDel, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        try:
            django_interface .delete_lab(labToDel)
        except Exception as e:
            return "Lab unsuccessfully deleted"
        return "Lab successfully deleted"

    def add_student_to_lab(self, labnumberP, userToAddP, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1': #might need to change
            return "Illegal permissions to do this action"
        try:
            l = django_interface .getLab(labnumberP)
        except Exception as e:
            return("Lab does not exist")

        if l.ParentCourse is None:
            return("Trying to to a lab secton which is not assigned a course")

        try:
            u = django_interface .login_username(userToAddP)
        except Exception as e:
            return("User you're trying to add to lab section does not exist")

        #Further error checking here. Put error check in django interface here?
        try:
           django_interface .add_student_to_lab(l, u)
        except Exception as e:
            print(e)
            return "Failed to add user to lab."
        return "User successfully added to lab"

    def add_lab_section_to_course(self, labnumberP, courseIDP, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        try:
            l = django_interface .getLab(labnumberP)
        except Exception as e:
            return("Lab does not exist")

        if l.ParentCourse is not None:
            return("Lab section already has a parent course")

        try:
            c = django_interface .getCourse(courseIDP)
        except Exception as e:
            return("Parent course you're trying to assign does not exist")

        try:
            django_interface .add_lab_section_to_course(l, c)
        except Exception as e:
            print(e)
            return "Failed to add lab section to course."
        return "Lab section successfully added to course"

    def assign_ta_to_lab(self, labnumber, ta, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        try:
            u = User.objects.get(username=ta)
        except Exception as e:
            return "TA does not exist"
        if u.permissions[3] != '1':
            return "The TA you're trying to assign does not have correct permissions (XXX1)"

        try:
            django_interface .assign_ta_to_lab(labnumber, ta)
        except Exception as e:
            print(e)
            return "Failed to assign ta to lab"
        return "TA successfully assigned to lab"