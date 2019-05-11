from django.test import TestCase
from UserEdits import UserEdits
from Notification import Notification
from DataRetrieval import DataRetrieval
from datetime import datetime, timedelta
from CourseEdit import CourseEdit
from Final.models import User


class UnitTests(TestCase):

    def setUp(self):
        # Setting up mock database
        self.supervisor = User.objects.create(username="superu", password="superpass", permissions="1000",
                                              address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        self.admin = User.objects.create(username="admin", password="adminpass", permissions="0111",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        self.ta = User.objects.create(username="tausername", password="tapassword", permissions="0001",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        self.instructor = User.objects.create(username="instructorU", password="instructorPass", permissions="0010",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        self.userNoPriv = User.objects.create(username="usernopriv", password="usernoprivpass", permissions="0000",
                                              address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        self.testuser = User.objects.create(username="testuser", password="testuserpass", permissions="0000",
                                              address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")

    u = UserEdits()
    n = Notification()
    c = CourseEdit()
    d = DataRetrieval()

    def test_add_userUnsuccessful(self):
        self.assertEqual(self.u.add_user("bad", "bad", "-1", "home", "4141231234", "student@gmail.com", self.admin), "Failed to add user. Improper parameters")

    def test_add_user_TA_NoPermission(self):
        self.assertEqual(self.u.add_user("UserName", "userpassword", "0001", "home", "4141231234", "student@gmail.com", self.ta),
                         "Illegal permissions to do this action")

    def test_add_user_Instructor_NoPermission(self):
        self.assertEqual(self.u.add_user("UserName", "password", "0001", "home", "4141231234", "student@gmail.com", self.instructor),
                         "Illegal permissions to do this action")

    def test_add_user_Admin_Successful(self):
        self.assertEqual("User successfully added", self.u.add_user("UserName", "password", "0001", "home", "4141231234", "student@gmail.com", self.admin))


    def test_add_user_Supervisor_Successful(self):
        self.assertEqual(self.u.add_user("UserName", "password", "0001", "home", "4141231234", "student@gmail.com", self.supervisor), "User successfully added")

    def test_add_user_Admin_Failed(self):
        self.assertEqual(self.u.add_user(" ", "password", "0001", "home", "4141231234", "studgmailcom", self.admin), "Failed to add user. Improper parameters")

    def test_add_user_Supervisor_Failed(self):
        self.assertEqual(self.u.add_user("UserName", " ", "0001", "home", "4141231234", "studgmail.com",  self.supervisor), "Failed to add user. Improper parameters")

    def test_delete_user_TA_NoPermission(self):
        self.assertEqual(self.u.delete_user(1, self.ta), "Illegal permissions to do this action")

    def test_delete_user_Instructor_NoPermission(self):
        self.assertEqual(self.u.delete_user(1, self.instructor), "Illegal permissions to do this action")

    def test_delete_user_Admin_FailedToDelete(self):
        self.assertEqual(self.u.delete_user(-1, self.admin), "User unsuccessfully deleted")

    def test_delete_user_Supervisor_FailedToDelete(self):
        self.assertEqual(self.u.delete_user(-1, self.supervisor), "User unsuccessfully deleted")

    def test_delete_user_Supervisor_FailedToDelete_Cannot_Delete_Self(self):
        self.assertEqual(self.u.delete_user("superu", self.supervisor), "Unable to delete active user")

    def test_delete_user_Admin_SuccessDelete(self):
        self.assertEqual(self.u.delete_user("testuser", self.admin), "User successfully deleted")

    def test_delete_user_Supervisor_SuccessToDelete(self):
        self.assertEqual(self.u.delete_user("testuser", self.supervisor), "User successfully deleted")

    def test_ChangeUser_Admin_IllegalField(self):
        self.assertEqual(self.u.change_contact("User", "NewField", "BadField"), "Illegal changed field")

    def test_ChangeUser_Supervisor_IllegalField(self):
        self.assertEqual(self.u.change_contact("User","NewField", "BadField"),
                         "Illegal changed field")

    def test_ChangeUser_Admin_IllegalChangedField(self):
        self.assertEqual(self.u.change_contact("User", "***a!`", "Name"), "Illegal changed field")

    def test_ChangeUser_Supervisor_IllegalChangedField(self):
        self.assertEqual(self.u.change_contact("User","***a!`", "Name"), "Illegal changed field")

    def test_ChangeUser_Admin_Success(self):
        self.assertEqual(self.u.change_contact("admin", "password", "Name"), "Contact information changed")

    def test_ChangeUser_Supervisor_Success(self):
        self.assertEqual(self.u.change_contact("superu","password", "Name"), "Contact information changed")

    def test_edit_user_TA_NoPermission(self):
        self.assertEqual(self.u.edit_user("testuser","username", "NewName", self.ta), "Illegal permissions to do this action")

    def test_edit_user_Instructor_NoPermission(self):
        self.assertEqual(self.u.edit_user("testuser","username", "NewName", self.instructor),
                         "Illegal permissions to do this action")

    def test_edit_user_Admin_UserDNE(self):
        self.assertEqual(self.u.edit_user("userdne", "username", "NewName", self.admin),
                         "Failed to update user")

    def test_edit_user_Supervisor_UserDNE(self):
        self.assertEqual(self.u.edit_user("superdne", "username", "NewName", self.supervisor),
                         "Failed to update user")

    def test_edit_user_Admin_IllegalFieldChange(self):
        self.assertEqual(self.u.edit_user("testuser", "IllegalField", "NewName", self.admin),
                         "Tried to change illegal field")

    def test_edit_user_Supervisor_IllegalFieldChange(self):
        self.assertEqual(self.u.edit_user("testuser", "IllegalField", "NewName", self.supervisor),
                         "Tried to change illegal field")

    def test_edit_user_Admin_IllegalChangedField(self):
        self.assertEqual(self.u.edit_user("testuser", "username", "****", self.admin), "Failed to updated user")

    def test_edit_user_Supervisor_IllegalChangedField(self):
        self.assertEqual(self.u.edit_user("testuser", "username", "****", self.supervisor), "Failed to updated user")

    def test_edit_user_Admin_SuccessfulChange(self):
        self.assertEqual(self.u.edit_user("testuser", "username", "NewName", self.admin), "User successfully updated")

    def test_edit_user_Supervisor_SuccessfulChange(self):
        self.assertEqual(self.u.edit_user("testuser","username", "NewName", self.supervisor), "User successfully updated")

    def test_SendNotification_TA_NoPermission(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", "subject", "body", self.ta),
                         "Illegal permissions to do this action")

    def test_SendNotification_Instructor_NoPermission(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", "subject", "body", self.instructor),
                         "Illegal permissions to do this action")

    def test_SendNotification_Admin_FromAddressDNE(self):
        self.assertEqual(self.n.send_email("notindatabse@gmail.com", "to@gmail.com", "subject", "body", self.admin),
                         "From user does not exist")

    def test_SendNotification_Supervisor_FromAddressDNE(self):
        self.assertEqual(
            self.n.send_email("notindatabase@gmail.com", "to@gmail.com", "subject", "body", self.supervisor),
            "From user does not exist")

    def test_SendNotification_Admin_ToAddressDNE(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "notindatabase@gmail.com", "subject", "body", self.admin),
                         "To user does not exist")

    def test_SendNotification_Supervisor_ToAddressDNE(self):
        self.assertEqual(
            self.n.send_email("from@gmail.com", "notindatabase@gmail.com", "subject", "body", self.supervisor),
            "To user does not exist")

    def test_SendNotification_Admin_IllegalEmailBody(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", "subject", "  ", self.admin),
                         "Illegal subject")

    def test_SendNotification_Supervisor_IllegalEmailBody(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", "subject", "  ", self.supervisor),
                         "Illegal subject")

    def test_SendNotification_Admin_IllegalEmailSubject(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", " ", "body", self.admin),
                         "Illegal email body")

    def test_SendNotification_Supervisor_IllegalEmailSubject(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", " ", "body", self.supervisor),
                         "Illegal email body")

    def test_SendNotification_Admin_Success(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", "subject", "body", self.admin),
                         "Email sent")

    def test_SendNotification_Supervisor_Success(self):
        self.assertEqual(self.n.send_email("from@gmail.com", "to@gmail.com", "subject", "body", self.supervisor),
                         "Email sent")

    def test_SendTaEmail_TA_NoPermission(self):
        self.assertEqual(self.n.send_email_to_ta("from@gmail", "to@gmail", "subject", "body", self.ta),
                         "You do not have permission")

    def test_SendTAEmail_Instructor_TADoesNotExist(self):
        self.assertEqual(
            self.n.send_email_to_ta("from@gmail", "nonexistantta@gmail", "subject", "body", self.instructor),
            "TA does not exist")

    def test_SendTAEmail_Instructor_IllegalFrom(self):
        self.assertEqual(
            self.n.send_email_to_ta("doesnotexist@gmail.com", "to@gmail.com", "subject", "body", self.instructor),
            "From user does not exist")

    def test_SendTAEmail_Instructor_IllegalEmailBody(self):
        self.assertEqual(
            self.n.send_email_to_ta("from@gmail.com", "to@gmail.com", "subject", " ", self.instructor),
            "Illegal email body")

    def test_SendTAEmail_Instructor_IllegalEmailSubject(self):
        self.assertEqual(
            self.n.send_email_to_ta("from@gmail.com", "to@gmail.com", " ", "body", self.instructor),
            "Illegal subject")

    def test_SendTAEmail_Instructor_Success(self):
        self.assertEqual(
            self.n.send_email_to_ta("from@gmail.com", "to@gmail.com", "subject", "body", self.instructor),
            "Email sent to TAs successfully")

    def test_SendTAEmail_Admin_Success(self):
        self.assertEqual(
            self.n.send_email_to_ta("from@gmail.com", "to@gmail.com", "subject", "body", self.admin),
            "Email sent to TAs successfully")

    def test_SendTAEmail_Supervisor_Success(self):
        self.assertEqual(
            self.n.send_email_to_ta("from@gmail.com", "to@gmail.com", "subject", "body", self.supervisor),
            "Email sent to TAs successfully")

    def test_view_all_courses_TA_NoCourses(self):
        self.assertEqual(self.c.view_all_courses(self.ta), "No courses")

    def test_view_all_courses_TA_Courses(self):
        self.assertEqual(self.c.view_all_courses(self.ta), "List of classes: ")

    def test_view_all_courses_Instructor_Courses(self):
        self.assertEqual(self.c.view_all_courses(self.instructor), "List of classes: ")

    def test_view_all_courses_Admin_Courses(self):
        self.assertEqual(self.c.view_all_courses(self.admin), "List of classes: ")

    def test_view_all_courses_Supervisor_Courses(self):
        self.assertEqual(self.c.view_all_courses(self.supervisor), "List of classes: ")

    def test_assign_ta_TA_NoPermission(self):
        self.assertEqual(self.c.assign_ta("ta", 1, 800, self.ta), "Do not have permissions for this action")

    def test_assign_ta_Instructor_TADNE(self):
        self.assertEqual(self.c.assign_ta("TADoesNotExist", 1, 800, self.instructor), "Ta does not exist")

    def test_assign_ta_Instructor_CourseDNE(self):
        self.assertEqual(self.c.assign_ta("taInDatabase", -1, 800, self.instructor), "Course section does not exist")

    def test_assign_ta_Instructor_LabSectionDNE(self):
        self.assertEqual(self.c.assign_ta("taInDatabase", 1, -1, self.instructor), "Lab section does not exist")

    def test_assign_ta_Instructor_Success(self):
        self.assertEqual(self.c.assign_ta("taInDatabase", 1, 800, self.instructor), "TA assigned to Course/Lab section")

    def test_assign_ta_Admin_Success(self):
        self.assertEqual(self.c.assign_ta("taInDatabase", 1, 800, self.admin), "TA assigned to Course/Lab section")

    def test_assign_ta_Supervisor_Success(self):
        self.assertEqual(self.c.assign_ta("taInDatabase", 1, 800, self.supervisor), "TA assigned to Course/Lab section")

    def test_create_course_TA_NoPermission(self):
        self.assertEqual(
            self.c.create_course("instructorInDB", "courseInDb",  datetime.now(), datetime.now(), self.ta),
            "Illegal permissions to do this action")

    def testcreate_course_Instructor_NoPermission(self):
        self.assertEqual(
            self.c.create_course("instructorInDB", "courseInDb",  datetime.now(), datetime.now(), self.instructor),
            "Illegal permissions to do this action")

    def testcreate_course_Admin_InvalidTeacher(self):
        self.assertEqual(
            self.c.create_course("instructorNotInDb", "courseInDb", datetime.now(), datetime.now(), self.admin),
            "Teacher entered does not exist")

    def test_create_course_Admin_IllegalClassId(self):
        self.assertEqual(
            self.c.create_course("instructorU", "@@@@@", datetime.now(), datetime.now(), self.admin),
            "Illegal class id")

    def test_create_course_Admin_IllegalClassTime(self):
        self.assertEqual(
            self.c.create_course("instructorU", "courseInDb", datetime.now(), datetime.now() - timedelta(days=1), self.admin),
            "Illegal class time entered")

    def test_create_course_Admin_Success(self):
        self.assertEqual(
            self.c.create_course("instructorU", "courseInDb", datetime.now(), datetime.now() + timedelta(days=1),
                                 self.admin),
            "Course successfully added")

    def test_delete_course_TA_NoPermission(self):
        self.assertEqual(self.c.delete_course(1, self.ta), "Do not have permission to complete this action")

    def test_delete_course_Instructor_NoPermission(self):
        self.assertEqual(self.c.delete_course(1, self.instructor), "Do not have permission to complete this action")

    def test_delete_course_Admin_InvalidCourseId(self):
        self.assertEqual(self.c.delete_course(-1, self.admin), "Invalid course ID entered")

    def test_view_course_assignments_TA_NoPermission(self):
        self.assertEqual(self.d.get_all_courses(self.ta), "Illegal permissions to do this action")

    def test_view_course_assignments_Instructor_NoPermission(self):
        self.assertEqual(self.d.get_all_courses(self.instructor), "Illegal permissions to do this action")

    def test_view_course_assignments_Admin_CourseIdDNE(self):
        self.assertEqual(self.c.view_course_assignments(-1, self.admin), "Course does not exist")

    def test_view_course_assignments_Admin_Success(self):
        self.assertEqual(self.c.view_course_assignments(1, self.admin), "Course assignments: ")

    def test_view_course_assignments_Supervisor_Success(self):
        self.assertEqual(self.c.view_course_assignments(1, self.supervisor), "Course assignments: ")

    def test_view_database_get_info(self):
        list = self.d.view_database()
        self.assertEqual(len(list), 6)

