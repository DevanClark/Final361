from unittest import TestCase
from UserEdits import UserEdits
from User import User
from Notification import Notification
from DataRetrieval import DataRetrieval
from datetime import datetime, timedelta
from CourseEdit import CourseEdit


class UnitTests(TestCase):
    supervisor = User(1, "admin", "password", [1, 0, 0, 0], "address", "phoneNumber", "email")
    admin = User(1, "admin", "password", [0, 1, 0, 0], "address", "phoneNumber", "email")
    instructor = User(1, "admin", "password", [0, 0, 1, 0], "address", "phoneNumber", "email")
    ta = User(1, "admin", "password", [0, 0, 0, 1], "address", "phoneNumber", "email")
    userNoPriv = User(1, "test", "test", [0, 0, 0, 0], "addressT", "phoneNumberT", "emailT")
    u = UserEdits()
    n = Notification()
    c = CourseEdit()
    d = DataRetrieval()

    # before we are able to run these tests we need to establish
    # that "admin", "admin" is in the database with permissions
    # the test user will also be in the database but not have permissions to access these method
    # create tests users with ids

    def testAddUserUnsuccessful(self):
        self.assertEqual(self.u.addUser("bad", "bad", self.admin), "Failed to add user. Improper parameters")

    def testAddUser_TA_NoPermission(self):
        self.assertEqual(self.u.addUser("UserName", "userpassword", self.ta), "Illegal permissions to do this action")

    def testAddUser_Instructor_NoPermission(self):
        self.assertEqual(self.u.addUser("UserName", "password", self.instructor), "Illegal permissions to do this "
                                                                                  "action")

    def testAddUser_Admin_Successful(self):
        self.assertEqual(self.u.addUser("UserName", "password", self.admin), "User added")

    def testAddUser_Supervisor_Successful(self):
        self.assertEqual(self.u.addUser("UserName", "password", self.supervisor), "User added")

    def testAddUser_Admin_Failed(self):
        self.assertEqual(self.u.addUser("UserName", "password", self.admin), "Failed to add user")

    def testAddUser_Supervisor_Failed(self):
        self.assertEqual(self.u.addUser("UserName", "password", self.supervisor), "Failed to add user")

    def testDeleteUser_TA_NoPermission(self):
        self.assertEqual(self.u.deleteUser(1, self.ta), "Illegal permissions to do this action")

    def testDeleteUser_Instructor_NoPermission(self):
        self.assertEqual(self.u.deleteUser(1, self.instructor), "Illegal permissions to do this action")

    def testDeleteUser_Admin_FailedToDelete(self):
        self.assertEqual(self.u.deleteUser(-1, self.admin), "User unsuccesfully deleted")

    def testDeleteUser_Supervisor_FailedToDelete(self):
        self.assertEqual(self.u.deleteUser(-1, self.supervisor), "User unsuccesfully deleted")

    def testDeleteUser_Admin_SuccessDelete(self):
        self.assertEqual(self.u.deleteUser(1, self.admin), "User successfully deleted")

    def testDeleteUser_Supervisor_SuccessToDelete(self):
        self.assertEqual(self.u.deleteUser(1, self.supervisor), "User succesfully deleted")

    def testChangeUser_Admin_IllegalField(self):
        self.assertEqual(self.u.changeContact("NewField", "BadField", self.admin), "Tried to change illegal field")

    def testChangeUser_Supervisor_IllegalField(self):
        self.assertEqual(self.u.changeContact("NewField", "BadField", self.supervisor), "Tried to change illegal field")

    def testChangeUser_Admin_IllegalChangedField(self):
        self.assertEqual(self.u.changeContact("***a!`", "Name", self.admin), "Illegal changed field")

    def testChangeUser_Supervisor_IllegalChangedField(self):
        self.assertEqual(self.u.changeContact("***a!`", "Name", self.supervisor), "Illegal changed field")

    def testChangeUser_Admin_Success(self):
        self.assertEqual(self.u.changeContact("NewName", "Name", self.admin), "Contact information changed")

    def testChangeUser_Supervisor_Success(self):
        self.assertEqual(self.u.changeContact("NewName", "Name", self.supervisor), "Contact information changed")

    def testEditUser_TA_NoPermission(self):
        self.assertEqual(self.u.editUser(1, "Name", "NewName", self.ta), "Illegal permissions to do this action")

    def testEditUser_Instructor_NoPermission(self):
        self.assertEqual(self.u.editUser(1, "Name", "NewName", self.instructor),
                         "Illegal permissions to do this action")

    def testEditUser_Admin_UserDNE(self):
        self.assertEqual(self.u.editUser(-1, "Name", "NewName", self.admin),
                         "User does not exist")

    def testEditUser_Supervisor_UserDNE(self):
        self.assertEqual(self.u.editUser(-1, "Name", "NewName", self.supervisor),
                         "User does not exist")

    def testEditUser_Admin_IllegalFieldChange(self):
        self.assertEqual(self.u.editUser(1, "IllegalField", "NewName", self.admin),
                         "Tried to change illegal field")

    def testEditUser_Supervisor_IllegalFieldChange(self):
        self.assertEqual(self.u.editUser(1, "IllegalField", "NewName", self.supervisor),
                         "Tried to change illegal field")

    def testEditUser_Admin_IllegalChangedField(self):
        self.assertEqual(self.u.editUser(1, "Name", "****", self.admin), "Illegal changed field")

    def testEditUser_Supervisor_IllegalChangedField(self):
        self.assertEqual(self.u.editUser(1, "Name", "****", self.supervisor), "Illegal changed field")

    def testEditUser_Admin_SuccessfulChange(self):
        self.assertEqual(self.u.editUser(1, "Name", "NewName", self.admin), "User successfully edited")

    def testEditUser_Supervisor_SuccessfulChange(self):
        self.assertEqual(self.u.editUser(1, "Name", "NewName", self.supervisor), "User successfully edited")

    def testSendNotification_TA_NoPermission(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", "subject", "body", self.ta),
                         "Illegal permissions to do this action")

    def testSendNotification_Instructor_NoPermission(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", "subject", "body", self.instructor),
                         "Illegal permissions to do this action")

    def testSendNotification_Admin_FromAddressDNE(self):
        self.assertEqual(self.n.sendEmail("notindatabse@gmail.com", "to@gmail.com", "subject", "body", self.admin),
                         "From user does not exist")

    def testSendNotification_Supervisor_FromAddressDNE(self):
        self.assertEqual(
            self.n.sendEmail("notindatabase@gmail.com", "to@gmail.com", "subject", "body", self.supervisor),
            "From user does not exist")

    def testSendNotification_Admin_ToAddressDNE(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "notindatabase@gmail.com", "subject", "body", self.admin),
                         "To user does not exist")

    def testSendNotification_Supervisor_ToAddressDNE(self):
        self.assertEqual(
            self.n.sendEmail("from@gmail.com", "notindatabase@gmail.com", "subject", "body", self.supervisor),
            "To user does not exist")

    def testSendNotification_Admin_IllegalEmailBody(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", "subject", "  ", self.admin),
                         "Illegal subject")

    def testSendNotification_Supervisor_IllegalEmailBody(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", "subject", "  ", self.supervisor),
                         "Illegal subject")

    def testSendNotification_Admin_IllegalEmailSubject(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", " ", "body", self.admin),
                         "Illegal email body")

    def testSendNotification_Supervisor_IllegalEmailSubject(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", " ", "body", self.supervisor),
                         "Illegal email body")

    def testSendNotification_Admin_Success(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", "subject", "body", self.admin),
                         "Email sent")

    def testSendNotification_Supervisor_Success(self):
        self.assertEqual(self.n.sendEmail("from@gmail.com", "to@gmail.com", "subject", "body", self.supervisor),
                         "Email sent")

    def testSendTaEmail_TA_NoPermission(self):
        self.assertEqual(self.n.sendEmailToTA("from@gmail", "to@gmail", "subject", "body", self.ta),
                         "You do not have permission")

    def testSendTAEmail_Instructor_TADoesNotExist(self):
        self.assertEqual(self.n.sendEmailToTA("from@gmail", "nonexistantta@gmail", "subject", "body", self.instructor),
                         "TA does not exist")

    def testSendTAEmail_Instructor_IllegalFrom(self):
        self.assertEqual(
            self.n.sendEmailToTA("doesnotexist@gmail.com", "to@gmail.com", "subject", "body", self.instructor),
            "From user does not exist")

    def testSendTAEmail_Instructor_IllegalEmailBody(self):
        self.assertEqual(
            self.n.sendEmailToTA("from@gmail.com", "to@gmail.com", "subject", " ", self.instructor),
            "Illegal email body")

    def testSendTAEmail_Instructor_IllegalEmailSubject(self):
        self.assertEqual(
            self.n.sendEmailToTA("from@gmail.com", "to@gmail.com", " ", "body", self.instructor),
            "Illegal subject")

    def testSendTAEmail_Instructor_Success(self):
        self.assertEqual(
            self.n.sendEmailToTA("from@gmail.com", "to@gmail.com", "subject", "body", self.instructor),
            "Email sent to TAs successfully")

    def testSendTAEmail_Admin_Success(self):
        self.assertEqual(
            self.n.sendEmailToTA("from@gmail.com", "to@gmail.com", "subject", "body", self.admin),
            "Email sent to TAs successfully")

    def testSendTAEmail_Supervisor_Success(self):
        self.assertEqual(
            self.n.sendEmailToTA("from@gmail.com", "to@gmail.com", "subject", "body", self.supervisor),
            "Email sent to TAs successfully")

    def testViewAllCourses_TA_NoCourses(self):
        self.assertEqual(self.c.viewAllCourses(self.ta), "No courses")

    def testViewAllCourses_TA_Courses(self):
        self.assertEqual(self.c.viewAllCourses(self.ta), "List of classes: ")

    def testViewAllCourses_Instructor_Courses(self):
        self.assertEqual(self.c.viewAllCourses(self.instructor), "List of classes: ")

    def testViewAllCourses_Admin_Courses(self):
        self.assertEqual(self.c.viewAllCourses(self.admin), "List of classes: ")

    def testViewAllCourses_Supervisor_Courses(self):
        self.assertEqual(self.c.viewAllCourses(self.supervisor), "List of classes: ")

    def testAssignTa_TA_NoPermission(self):
        self.assertEqual(self.c.assignTA("ta", 1, 800, self.ta), "Do not have permissions for this action")

    def testAssignTa_Instructor_TADNE(self):
        self.assertEqual(self.c.assignTA("TADoesNotExist", 1, 800, self.instructor), "Ta does not exist")

    def testAssignTa_Instructor_CourseDNE(self):
        self.assertEqual(self.c.assignTA("taInDatabase", -1, 800, self.instructor), "Course section does not exist")

    def testAssignTA_Instructor_LabSectionDNE(self):
        self.assertEqual(self.c.assignTA("taInDatabase", 1, -1, self.instructor), "Lab section does not exist")

    def testAssignTA_Instructor_Success(self):
        self.assertEqual(self.c.assignTA("taInDatabase", 1, 800, self.instructor), "TA assigned to Course/Lab section")

    def testAssignTA_Admin_Success(self):
        self.assertEqual(self.c.assignTA("taInDatabase", 1, 800, self.admin), "TA assigned to Course/Lab section")

    def testAssignTA_Supervisor_Success(self):
        self.assertEqual(self.c.assignTA("taInDatabase", 1, 800, self.supervisor), "TA assigned to Course/Lab section")

    def testCreateCourse_TA_NoPermission(self):
        self.assertEqual(
            self.c.createCourse("instructorInDB", 1, datetime.now(), "studentList", "labsection", "talist",
                                self.ta),
            "Do not have permission to access this action")

    def testCreateCourse_Instructor_NoPermission(self):
        self.assertEqual(
            self.c.createCourse("instructorInDB", 1, datetime.now(), "studentList", "labsection", "talist",
                                self.instructor),
            "Do not have permission to access this action")

    def testCreateCourse_Admin_InvalidTeacher(self):
        self.assertEqual(
            self.c.createCourse("instructorNotInDb", 1, datetime.now(), "studentList", "labsection", "talist",
                                self.admin),
            "Teacher entered does not exist")

    def testCreateCourse_Admin_IllegalClassId(self):
        self.assertEqual(
            self.c.createCourse("instructorInDb", -1, datetime.now(), "studentList", "labsection", "talist",
                                self.admin),
            "Illegal class id")

    def testCreateCourse_Admin_IllegalClassTime(self):
        self.assertEqual(
            self.c.createCourse("instructorInDB", 1, datetime.now() - timedelta(days=1), "studentList", "labsection",
                                "talist", self.admin),
            "Illegal class time entered")

    def testCreateCourse_Admin_TADNE(self):
        self.assertEqual(
            self.c.createCourse("instructorInDB", 1, datetime.now(), "studentList", "labsection", "invalidTA",
                                self.instructor), "TA specified does not exist")

    def testCreateCourse_Admin_IllegalLabNumber(self):
        self.assertEqual(
            self.c.createCourse("instructorInDB", 1, datetime.now(), "studentList", "-0001", "talist",
                                self.admin), "Illegal lab section number")

    def testCreateCourse_Admin_Success(self):
        self.assertEqual(
            self.c.createCourse("instructorInDB", 1, datetime.now(), "studentList", "labsection", "talist",
                                self.instructor),
            "Course added to the database")

    def testDeleteCourse_TA_NoPermission(self):
        self.assertEqual(self.c.deleteCourse(1, self.ta), "Do not have permission to complete this action")

    def testDeleteCourse_Instructor_NoPermission(self):
        self.assertEqual(self.c.deleteCourse(1, self.instructor), "Do not have permission to complete this action")

    def testDeleteCourse_Admin_InvalidCourseId(self):
        self.assertEqual(self.c.deleteCourse(-1, self.admin), "Invalid course ID entered")

    def testViewCourseAssignments_TA_NoPermission(self):
        self.assertEqual(self.c.viewCourseAssignments(1, self.ta), "Incorrect permission")

    def testViewCourseAssignments_Instructor_NoPermission(self):
        self.assertEqual(self.c.viewCourseAssignments(1, self.instructor), "Incorrect permission")

    def testViewCourseAssignments_Admin_CourseIdDNE(self):
        self.assertEqual(self.c.viewCourseAssignments(-1, self.admin), "Course does not exist")

    def testViewCourseAssignments_Admin_Success(self):
        self.assertEqual(self.c.viewCourseAssignments(1, self.admin), "Course assignments: ")

    def testViewCourseAssignments_Supervisor_Success(self):
        self.assertEqual(self.c.viewCourseAssignments(1, self.supervisor), "Course assignments: ")

    def testViewDatabase_TA_NoPermission(self):
        self.assertEqual(self.d.viewDatabase(self.ta), "Incorrect permissions")

    def testViewDatabase_Instructor_NoPermission(self):
        self.assertEqual(self.d.viewDatabase(self.instructor), "Incorrect permissions")

    def testViewDatabase_Admin_Success(self):
        self.assertEqual(self.d.viewDatabase(self.admin), "Data gathered")

    def testViewDatabase_Supervisor_Success(self):
        self.assertEqual(self.d.viewDatabase(self.supervisor), "Data gathered")
