from django.test import TestCase
from App import App
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Login import Login
from Final.DjangoInterface import DjangoInterface
from Final.models import User


class TestApp(TestCase):

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
        self.assertEqual("User logged in", result3)  # Username and password exist in the database.

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
        result1 = a.command("add_user newUsername newPassword 0000")
        a.command("logout")
        a.command("login testUsername testPassword")
        result2 = a.command("add_user ***** newPassword 0000")
        result3 = a.command("add_user username * 0000")
        result4 = a.command("add_user newUsername newPassword 0000")
        # Error cases
        self.assertEqual("Illegal permissions to do this action", result1)
        self.assertEqual("Failed to add user. Improper parameters", result2)
        self.assertEqual("Failed to add user. Improper parameters", result3)
        # Success
        self.assertEqual("User successfully added", result4)
        a.command("logout")

    def test_delete_user(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())

        a.command("login brokenUsername brokenPassword")
        result1 = a.command("delete_user delUsername")
        a.command("logout")
        a.command("login testUsername testPassword")
        result2 = a.command("delete_user BadUsername")
        result4 = a.command("delete_user delUsername")
        # Error cases
        self.assertEqual("Illegal permissions to do this action", result1)
        self.assertEqual("User unsuccessfully deleted", result2)
        # Success
        self.assertEqual("User successfully deleted", result4)
        a.command("logout")

    def test_change_contact_info(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login testUsername testPassword")
        result1 = a.command("change_contact testUsername name SAUCE")
        result2 = a.command("change_contact testUsername username *")
        result3 = a.command("change_contact testUsername address newaddress")
        # Error cases
        self.assertEqual("Illegal changed field", result1)  # Tried to change an illegal field
        self.assertEqual("Invalid parameter for this command",
                         result2)  # Updated field was illegal, contact field valid.
        # Success
        self.assertEqual("Contact information changed", result3)

    def test_edit_user_no_permissions(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login brokenUsername brokenPassword")
        result = a.command("edit_user username field update")
        # Error cases
        self.assertEqual("Illegal permissions to do this action", result)

    def test_edit_user_does_not_exist(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login testUsername testPassword")
        result = a.command("edit_user userdne username field")
        # Error cases
        self.assertEqual("Failed to update user", result)

    def test_edit_user_illegal(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login testUsername testPassword")
        result = a.command("edit_user userdne namedne field")
        self.assertEqual("Tried to change illegal field", result)  # Tried to change an illegal field

    def test_edit_user_success(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        a.command("login testUsername testPassword")
        result = a.command("edit_user testUsername username newname")
        self.assertEqual("User successfully updated", result)  # Tried to change an illegal field

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

    def test_send__TA_email(self):
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
    def test_view__all_classes(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("LoggedInUser")
        # Error cases
        self.assertEqual("Not enrolled in any classes", result)
        # Success
        self.assertEqual("List of classes: ", result)

    def test_assign_TA(self):
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

    def test_create_course(self):
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

    def test_delete_course(self):
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

    def test_view_course_assignments(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("CourseID LoggedInUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("Illegal course ID entered", result)
        # Success
        self.assertEqual("Course assignments: ", result)

    # DataRetrieval
    def test_ViewDatabase(self):
        a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
        result = a.command("LoggedInUser")
        # Error cases
        self.assertEqual("Illegal permissions to do this activity", result)
        self.assertEqual("Error while connecting to the database", result)
        # Success
        self.assertEqual("Data gathered", result)

    def test_createuser(self):
        result1= #page renders correctly
        result2= #correct input results in new user
        result3= #incorrent input returns the proper string response

    def test_edituserself(self):
        result1= #page renders correctly
        result2-X= #correct input results in changed field
        resultX+1= #incorrect input results in proper string response

    def test_landingpage(self):
        result1= #page renders correctly

    def test_loginpage(self):
        result1= #page renders correctly
        result2= #correct input logs someone in
        result3-4= #incorrect input returns proper string response (user doesn't exist vs username/pass incorrect)

    def test_base(self):
        result1= #homepage renders correctly from link
        result2-X= #pages render correctly from linkss

    def test_commandform(self):
        result1= #fields render
        result2-X= #correct input returns proper output (CommandFormResult)
        resultX+1-Y= #incorrect input returns proper string output

    def test_commandformresult(self):
        result1= #page renders correctly
