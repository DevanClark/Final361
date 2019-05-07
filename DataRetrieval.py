from Final import DjangoInterface
from Final.models import *

class DataRetrieval:

    def __init__(self):
        self = self

    def view_enrolled_courses(self, logged_in_user):
        u = User.objects.get(username=logged_in_user.username)
        c = Course.objects.filter(self, )

    def view_ta_assignments(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1' and logged_in_user.permissions[2] != '1':
            return "Illegal permissions to do this action"

        listofTAs = User.objects.filter(permissions="0001")
        return listofTAs

    def view_database(self, loggedinuser):
        return "yes"

