from Final.DjangoInterface import DjangoInterface
from Final.models import *
from WorkingModels.TaClasses import TaClasses
d = DjangoInterface()

class DataRetrieval:

    def init(self):
        self = self

    def view_enrolled_courses(self, logged_in_user):
        u = User.objects.get(username=logged_in_user.username)
        c = Course.objects.filter(self, )

    def get_ta_assignments(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1' and logged_in_user.permissions[2] != '1':
            return "Illegal permissions to do this action"
        try:
            all_courses = d.get_all_courses()
        except Exception as e:
            return "Unable to get any current teaching assistants"
        return all_courses

    def get_classes_by_instructor(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1' and logged_in_user.permissions[2] != '1':
            return "Illegal permissions to do this action"
        try:
            all_classes_for_instructor = d.get_all_classes_by_instructor(logged_in_user.username)
        except Exception as e:
            return "Unable to find any courses for this instructor"
        return all_classes_for_instructor
