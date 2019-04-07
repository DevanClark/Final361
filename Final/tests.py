from django.test import TestCase
from User import User
from App import App
from Course import Course
from UserEdits import UserEdits
from CourseEdit import CourseEdit


class TestApp(TestCase):

    testUser = User("testUsername", "testPassword", [1, 1, 1, 1])
    brokenTestUser = User("brokenUsername", "brokenPassword", [0, 0, 0, 0])
    deleteMeUser = User("delUsername", "delPassword", [0, 0, 0, 0])
    testTAUser = User("TAUsername", "TAPassword", [0, 0, 0, 1])
    testCourse = Course(101, "8:00", "12:00", [801])
    deleteMeCourse = Course(999, "0:00", "24:00", [999])
    a = App(CourseEdit, User, UserEdits)

    def test_login_to_database(self):
        # assume username is in the directory/database
        result1 = self.a.command("login_to_database BadUser testPassword")  # There's no user logged in???
        result2 = self.a.command("login_to_database testUsername BadPass")
        result3 = self.a.command("login_to_database testUsername testPassword")
        # Error cases
        self.assertEqual("Incorrect username/password", result1)  # Username will trip this failure first.
        self.assertEqual("Incorrect username/password", result2)  # Result will contain an existing user with a bad pass
        # Success
        self.assertEqual("User logged in", result3)      # Username and password exist in the database.

    def test_logout(self):
        result = self.a.command("logout")
        # Error cases
        self.assertNotEqual("Logout was unsuccessful", result)
        # Success
        self.assertEqual("User logged out", result)

    def test_add_user(self):
        self.brokenTestUser.login_to_database("brokenUsername", "brokenPassword")
        result1 = self.a.command("add_user newUsername newPassword")
        self.brokenTestUser.logout()
        self.testUser.login_to_database("testUsername", "testPassword")
        result2 = self.a.command("add_user newBadUser newPassword")
        result3 = self.a.command("add_user newUsername newBadPass")
        result4 = self.a.command("add_user newUsername newPassword")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal username entered", result2)
        self.assertEqual("Illegal password entered", result3)
        # Success
        self.assertEqual("User successfully added", result4)
        self.testUser.logout()

    def test_delete_user(self):
        self.brokenTestUser.login_to_database("brokenUsername", "brokenPassword")
        result1 = self.a.command("delete_user delUsername delPassword")
        self.brokenTestUser.logout()
        self.testUser.login_to_database("testUsername", "testPassword")
        result2 = self.a.command("delete_user BadUsername delPassword")
        result3 = self.a.command("delete_user delUsername BadPassword")
        result4 = self.a.command("delete_user delUsername delPassword")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal username entered", result2)
        self.assertEqual("Illegal password entered", result3)
        # Success
        self.assertEqual("User successfully deleted", result4)
        self.testUser.logout()

    def test_change_contact_info(self):
        result = self.a.command("chenge_contact_info testUser.username SAUCE")
        # Error cases
        self.assertEqual("Tried to change illegal field", result)  # Tried to change an illegal field
        self.assertEqual("Illegal updated field", result)          # Updated field was illegal, contact field valid.
        # Success
        self.assertEqual("Contact information updated", result)

    def test_edit_user(self):
        result = self.a.command("User Field Updated Field UpdatedUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("User Does not exit", result)
        self.assertEqual("Tried to change illegal field", result)  # Tried to change an illegal field
        self.assertEqual("Illegal updated field", result)          # Updated field was illegal, contact field valid.
        # Success
        self.assertEqual("User successfully edited", result)

    def send_email(self):
        result = self.a.command("From To Subject Body User UpdatedUser")
        # Error cases
        self.assertEqual("From user does not exist", result)
        self.assertEqual("To user does not exist", result)
        self.assertEqual("Illegal email subject", result)
        self.assertEqual("Illegal email body", result)
        # Success
        self.assertEqual("Email successfully sent", result)

    def send__TA_email(self):
        result = self.a.command("From To Subject Body TA UpdatedUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("TA(s) do not exist", result)
        self.assertEqual("Illegal email subject", result)
        self.assertEqual("Illegal email body", result)
        # Success
        self.assertEqual("Email sent to TA(s) successfully", result)

# Course Edits tests
    def view__all_classes(self):
        result = self.a.command("LoggedInUser")
        # Error cases
        self.assertEqual("Not enrolled in any classes", result)
        # Success
        self.assertEqual("List of classes: ", result)

    def assign_TA(self):
        self.brokenTestUser.login_to_database("brokenUsername", "brokenPassword")
        result1 = self.a.command("assign_TA TAUsername 101 801")
        self.brokenTestUser.logout()
        self.testUser.login_to_database("testUsername", "testPassword")
        result2 = self.a.command("assign_TA badTAUsername 101 801")
        result3 = self.a.command("assign_TA TAUsername badID 801")
        result4 = self.a.command("assign_TA TAUsername 101 badLab")
        result5 = self.a.command("assign_TA TAUsername 101 801")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("TA(s) do not exist", result2)
        self.assertEqual("Course does not exist", result3)
        self.assertEqual("Lab section Does not exist", result4)
        # Success
        self.assertEqual("TA assigned to Course/Lab section", result5)
        self.testUser.logout()

    def create_course(self):
        self.brokenTestUser.login_to_database("brokenUsername", "brokenPassword")
        result1 = self.a.command("create_course 361 10:00 10:50 [801,802,803,804]")
        self.brokenTestUser.logout()
        self.testUser.login_to_database("testUsername", "testPassword")
        result2 = self.a.command("create_course badID 10:00 10:50 [801,802,803,804]")
        result3 = self.a.command("create_course 361 badTime 10:50 [801,802,803,804]")
        result4 = self.a.command("create_course 361 10:00 badTime [801,802,803,804]")
        result5 = self.a.command("create_course 361 10:00 10:50 [801,802,803,badLab]")
        result6 = self.a.command("create_course 361 10:00 10:50 [801,802,803,804]")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal class ID entered", result2)
        self.assertEqual("Illegal start time entered", result3)
        self.assertEqual("Illegal end time entered", result4)
        self.assertEqual("Illegal lab section(s) entered", result5)
        # Success
        self.assertEqual("Course added to the database", result6)
        self.testUser.logout()

    def delete_course(self):
        self.brokenTestUser.login_to_database("brokenUsername", "brokenPassword")
        result1 = self.a.command("delete_course 999")
        self.brokenTestUser.logout()
        self.testUser.login_to_database("testUsername", "testPassword")
        result2 = self.a.command("delete_course badID")
        result3 = self.a.command("delete_course 999")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result1)
        self.assertEqual("Illegal course ID entered", result2)
        # Success
        self.assertEqual("Course deleted from the database", result3)

    def view_course_assignments(self):
        result = self.a.command("CourseID LoggedInUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("Illegal course ID entered", result)
        # Success
        self.assertEqual("Course assignments: ", result)

# DataRetrvial
    def ViewDatabase(self):
        result = self.a.command("LoggedInUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("Error while connecting to the database", result)
        # Success
        self.assertEqual("Data gathered", result)
