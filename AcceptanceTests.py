from django.test import TestCase
from Final.models import models
from User import User
from App import App
#from Course import Course
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Login import Login
from Final.DjangoInterface import DjangoInterface
from Final.models import User

class TestApp(TestCase):
    #Old tests, maybe delete
    testUser = User("testUsername", "testPassword", [1, 1, 1, 1], "testAddress", "TestPhoneNum", "TestEmail")
    brokenTestUser = User("brokenUsername", "brokenPassword", [0, 0, 0, 0], "testAddress", "TestPhoneNum", "TestEmail")
    deleteMeUser = User("delUsername", "delPassword", [0, 0, 0, 0], "testAddress", "TestPhoneNum", "TestEmail")
    testTAUser = User("TAUsername", "TAPassword", [0, 0, 0, 1], "testAddress", "TestPhoneNum", "TestEmail")
    #testCourse = Course(101, "8:00", "12:00", [801])
    #deleteMeCourse = Course(999, "0:00", "24:00", [999])

    def setUp(self):
        # Setting up mock database
        User.objects.create(username="testUsername", password="testPassword", permissions="1111",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="brokenUsername", password="brokenPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="delUsername", password="delPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")

    def test_login_to_database(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        # assume username is in the directory/database
        result1 = a.command("login BadUser testPassword")
        result2 = a.command("login testUsername BadPass")
        result3 = a.command("login testUsername testPassword")
        # Error cases
        self.assertEqual("User does not exist", result1)  # Username will trip this failure first.
        self.assertEqual("Incorrect username/password", result2)  # Result will contain an existing user with a bad pass
        # Success
        self.assertEqual("User logged in", result3)      # Username and password exist in the database.

    def test_logout_success_(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        user = a.command("login testUsername testPassword")
        result = a.command("logout")
        self.assertEqual("User logged out", result)

    def test_logout_failed_not_loggedin(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("logout")
        self.assertEqual("User is not logged in", result)
        self.assertNotEqual("User logged out", result)

    def test_add_user(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())

        a.command("login brokenUsername brokenPassword")
        result1 = a.command("add_user newUsername newPassword")
        a.command("logout")
        a.command("login testUsername testPassword")
        result2 = a.command("add_user newBadUser newPassword")
        result3 = a.command("add_user newUsername newBadPass")
        result4 = a.command("add_user newUsername newPassword")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal username entered", result2)
        self.assertEqual("Illegal password entered", result3)
        # Success
        self.assertEqual("User successfully added", result4)
        a.command("logout")

    def test_delete_user(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())

        a.command("login brokenUsername brokenPassword")
        result1 = a.command("delete_user delUsername delPassword")
        a.command("logout")
        a.command("login testUsername testPassword")
        result2 = a.command("delete_user BadUsername delPassword")
        result3 = a.command("delete_user delUsername BadPassword")
        result4 = a.command("delete_user delUsername delPassword")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal username entered", result2)
        self.assertEqual("Illegal password entered", result3)
        # Success
        self.assertEqual("User successfully deleted", result4)
        a.command("logout")

    def test_change_contact_info(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("change_contact testUser.username SAUCE")
        # Error cases
        self.assertEqual("Tried to change illegal field", result)  # Tried to change an illegal field
        self.assertEqual("Illegal updated field", result)          # Updated field was illegal, contact field valid.
        # Success
        self.assertEqual("Contact information updated", result)

    def test_edit_user(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("User Field Updated Field UpdatedUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("User Does not exit", result)
        self.assertEqual("Tried to change illegal field", result)  # Tried to change an illegal field
        self.assertEqual("Illegal updated field", result)          # Updated field was illegal, contact field valid.
        # Success
        self.assertEqual("User successfully edited", result)

    def send_email(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("From To Subject Body User UpdatedUser")
        # Error cases
        self.assertEqual("From user does not exist", result)
        self.assertEqual("To user does not exist", result)
        self.assertEqual("Illegal email subject", result)
        self.assertEqual("Illegal email body", result)
        # Success
        self.assertEqual("Email successfully sent", result)

    def send__TA_email(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("From To Subject Body TA UpdatedUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("TA(s) do not exist", result)
        self.assertEqual("Illegal email subject", result)
        self.assertEqual("Illegal email body", result)
        # Success
        self.assertEqual("Email sent to TA(s) successfully", result)

# Course Edits tests
    def view__all_classes(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("LoggedInUser")
        # Error cases
        self.assertEqual("Not enrolled in any classes", result)
        # Success
        self.assertEqual("List of classes: ", result)

    def assign_TA(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login brokenUsername brokenPassword")
        result1 = a.command("assign_TA TAUsername 101 801")
        a.command("logout")
        a.command("login testUsername testPassword")
        result2 = a.command("assign_TA badTAUsername 101 801")
        result3 = a.command("assign_TA TAUsername badID 801")
        result4 = a.command("assign_TA TAUsername 101 badLab")
        result5 = a.command("assign_TA TAUsername 101 801")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("TA(s) do not exist", result2)
        self.assertEqual("Course does not exist", result3)
        self.assertEqual("Lab section Does not exist", result4)
        # Success
        self.assertEqual("TA assigned to Course/Lab section", result5)
        a.command("logout")

    def create_course(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login brokenUsername brokenPassword")
        result1 = a.command("create_course 361 10:00 10:50 [801,802,803,804]")
        a.command("logout")
        a.command("login testUsername testPassword")
        result2 = a.command("create_course badID 10:00 10:50 [801,802,803,804]")
        result3 = a.command("create_course 361 badTime 10:50 [801,802,803,804]")
        result4 = a.command("create_course 361 10:00 badTime [801,802,803,804]")
        result5 = a.command("create_course 361 10:00 10:50 [801,802,803,badLab]")
        result6 = a.command("create_course 361 10:00 10:50 [801,802,803,804]")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal class ID entered", result2)
        self.assertEqual("Illegal start time entered", result3)
        self.assertEqual("Illegal end time entered", result4)
        self.assertEqual("Illegal lab section(s) entered", result5)
        # Success
        self.assertEqual("Course added to the database", result6)
        a.command("logout")

    def delete_course(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login brokenUsername brokenPassword")
        result1 = a.command("delete_course 999")
        a.command("logout")
        a.command("login testUsername testPassword")
        result2 = a.command("delete_course badID")
        result3 = a.command("delete_course 999")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal course ID entered", result2)
        # Success
        self.assertEqual("Course deleted from the database", result3)

    def view_course_assignments(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("CourseID LoggedInUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("Illegal course ID entered", result)
        # Success
        self.assertEqual("Course assignments: ", result)

# DataRetrvial
    def ViewDatabase(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("LoggedInUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("Error while connecting to the database", result)
        # Success
        self.assertEqual("Data gathered", result)
