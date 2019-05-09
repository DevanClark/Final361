from Final import DjangoInterface
from Final.models import *

class LabEdit:
    def __init__(self):
        self = self

    def create_lab(self, TA, labnumber, starttime, endtime, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1': #can instructors create lab sections?
            return "Illegal permissions to do this action"

        #Move error cases to somewhere else?
        try:
            u = User.objects.get(username=TA) #Move to __init__?
        except Exception as e:
            return "The TA you're trying to assign does not exist"

        if u.permissions[3] != '1':
            return "The user you're trying to assign as a TA does not have TA-level permissions (xxx1)"

        #Further error checking here
        try:
            DjangoInterface.DjangoInterface.create_lab(self, labnumber, TA, starttime, endtime)
        except Exception as e:
            print(e)
            return "Failed to create lab."
        return "Lab successfully added"  # Whatever was written in the acceptance tests

    def delete_lab(self, labToDel, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        try:
            DjangoInterface.DjangoInterface.delete_lab(self, labToDel)
        except Exception as e:
            return "Lab unsuccessfully deleted"
        return "Lab successfully deleted"

    def add_student_to_lab(self, labnumberP, userToAddP, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1': #might need to change
            return "Illegal permissions to do this action"
        try:
            l = DjangoInterface.DjangoInterface.getLab(self, labnumberP)
        except Exception as e:
            return("Lab does not exist")

        if l.ParentCourse is None:
            return("Trying to to a lab secton which is not assigned a course")

        try:
            u = DjangoInterface.DjangoInterface.login_username(self, userToAddP)
        except Exception as e:
            return("User you're trying to add to lab section does not exist")

        #Further error checking here. Put error check in django interface here?
        try:
           DjangoInterface.DjangoInterface.add_student_to_lab(self, l, u)
        except Exception as e:
            print(e)
            return "Failed to add user to lab."
        return "User successfully added to lab"

    def add_lab_section_to_course(self, labnumberP, courseIDP, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        try:
            l = DjangoInterface.DjangoInterface.getLab(self, labnumberP)
        except Exception as e:
            return("Lab does not exist")

        if l.ParentCourse is not None:
            return("Lab section already has a parent course")

        try:
            c = DjangoInterface.DjangoInterface.getCourse(self, courseIDP)
        except Exception as e:
            return("Parent course you're trying to assign does not exist")

        try:
            DjangoInterface.DjangoInterface.add_lab_section_to_course(self, l, c)
        except Exception as e:
            print(e)
            return "Failed to add lab section to course."


        return "Lab section successfully added to course"
