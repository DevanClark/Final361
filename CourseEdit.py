
from Final import DjangoInterface
from Final.models import *

# The Course Edits class is designed to handle the creating, editing and deleting of courses within the app

class CourseEdit:
    def __init__(self):
        self = self

    # method to create a course in the database
    # There are 5 parameters
    # Instructor to be assigned to the course if desired
    # Course name is the name to be assigned to the course
    # Start time and End Time of the course
    # Logged_in_User is the user that is attempting to create a course
    def create_course(self, instructor, coursename, starttime, endtime, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        try:
            u = User.objects.get(username=instructor) #Move to __init__?

            if u.permissions[2] != '1':
                return "The user you're trying to assign as an instructor does not have instructor-level permissions (xx1x)"
        except Exception as e:
            # If the instructor pass in does not exist, set it to "None" to feed into the django_interface
            instructor = "None"

        try:
            DjangoInterface.DjangoInterface.create_course(self, instructor, coursename, starttime, endtime)
        except Exception as e:
            print(e)
            return "Failed to create course."
        return "Course successfully added"  # Whatever was written in the acceptance tests

    # Delete course method
    # courseToDel is the name of the course to be deleted
    # logged_in_user is the user attempting to delete the course from the database
    def delete_course(self, courseToDel, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        try:
            DjangoInterface.DjangoInterface.delete_course(self, courseToDel)
        except Exception as e:
            return "Course unsuccessfully deleted"
        return "Course successfully deleted"

    # Add User(student) to course
    # courseIDP is the course that the user(student) will be added to
    # logged_in_user is the user attempting to add a user to the course
    # note: Users are not limited to being students, a teacher or ta can be added as well
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

    # Add TA to course
    # courseIDP is the course the TA will be assigned to
    # logged_in_user is the user attempting to assign a TA
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

    def assign_instructor_to_course(self, courseIDP, instructorP, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        try:
            u = User.objects.get(username=instructorP)
        except Exception as e:
            return "Instructor does not exist"
        if u.permissions[2] != '1':
            return "The instructor you're trying to assign does not have correct permissions (XX1X)"

        try:
            DjangoInterface.DjangoInterface.assign_instructor_to_course(self, courseIDP, instructorP)
        except Exception as e:
            print(e)
            return "Failed to assign instructor to course"
        return "Instructor successfully assigned to course"

    # View all courses method
    # logged_in_user is the user attempting to view all the courses
    def view_all_courses(self, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"

        return "yes"

    # Assign_TA stub
    # note: Assigning TA's is handled in the lab creation
    def assign_ta(self, tausername, courseid, labsection, loggedinuser):
        return "yes"

    # View Course Assignment stub
    def view_course_assignments(self, courseid, loggedinuser):
        return "yes"


