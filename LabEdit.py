from Final import DjangoInterface
from Final.models import *

class LabEdit:
    def __init__(self):
        self = self

    def create_lab(self, TA, labnumber, starttime, endtime, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        #Move error cases to somewhere else? Feels like it's defeating the purpose of the django interface.
        try:
            u = User.objects.get(username=TA) #Move to __init__?
        except Exception as e:
            return "The TA you're trying to assign does not exist"

        if u.permissions[3] != '1':
            return "The user you're trying to assign as a TA does not have TA-level permissions (xxx1)"

        #Further error checking here

        try:
            DjangoInterface.DjangoInterface.create_lab(self, labnumber, TA, starttime, endtime,)
        except Exception as e:
            print(e)
            return "Failed to create lab."
        return "Lab successfully added"  # Whatever was written in the acceptance tests

    def delete_course(self, courseToDel, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        try:
            DjangoInterface.DjangoInterface.delete_course(self, courseToDel)
        except Exception as e:
            return "Course unsuccessfully deleted"
        return "Course successfully deleted"

    def add_user_to_course(self, courseIDP, userToAddP, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        #Further error checking here
        try:
            DjangoInterface.DjangoInterface.add_user_to_course(self, courseIDP, userToAddP)
        except Exception as e:
            print(e)
            return "Failed to add user to course."
        return "User successfully added to course"

    def add_TA_to_course(self, courseIDP, TAToAddP, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        #Again, move these error checks somewhere else?
        try:
            u = User.objects.get(username=TAToAddP)
        except Exception as e:
            return "TA does not exist"
        if u.permissions[3] != '1':
            return "The TA you're trying to assign does not have correct permissions (XXX1)"
        # Further error checking here

        try:
            DjangoInterface.DjangoInterface.add_TA_to_course(self, courseIDP, TAToAddP)
        except Exception as e:
            print(e)
            return "Failed to add TA to course."
        return "TA successfully added to course"

    def view_all_courses(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        return "yes"

    def assign_ta(self, tausername, courseid, labsection, loggedinuser):
        return "yes"

    def view_course_assignments(self, courseid, loggedinuser):
        return "yes"


