from Final import DjangoInterface
from Final.models import *

from Final.DjangoInterface import DjangoInterface
from Final.models import *

d = DjangoInterface()


class DataRetrieval:

    def view_ta_assignments(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1' and logged_in_user.permissions[2] != '1':
            return "Illegal permissions to do this action"
        listofTAs = User.objects.filter(permissions="0001")
        return listofTAs

    def get_all_courses(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        return d.get_all_courses()

    def view_database(self):
        return d.get_all_users_in_system()

    def get_all_labs(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        return d.get_all_labs()

    def get_ta_assignments(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1' and logged_in_user.permissions[2] != '1':
            return "Illegal permissions to do this action"
        try:
            all_courses = d.get_all_courses()
        except Exception as e:
            return "Unable to get any current teaching assistants"
        all_courses_with_a_ta = []
        for course in all_courses:
            if len(course.tas_per_course) > 0:
                all_courses_with_a_ta.append(course)
        if len(all_courses_with_a_ta) == 0:
            return "No Tas in this course"
        return all_courses

    def get_classes_by_instructor(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1' and logged_in_user.permissions[
            2] != '1':
            return "Illegal permissions to do this action"
        try:
            all_classes_for_instructor = d.get_all_classes_by_instructor(logged_in_user.username)
        except Exception as e:
            return "Unable to find any courses for this instructor"
        return all_classes_for_instructor

    def get_classes_by_ta(self, logged_in_user):
        if "1" not in logged_in_user.permissions:
            return "Illegal permissions to do this action"
        try:
            all_courses = d.get_all_courses()
        except Exception as e:
            return "Unable to get any current teaching assistants"
        all_ta_courses = []
        for course in all_courses:
            for ta in course.tas_per_course:
                if ta.username == logged_in_user.username:
                    all_ta_courses.append(course)
        if len(all_ta_courses) == 0:
            return "You are not enrolled in any courses"
        else:
            return all_ta_courses
