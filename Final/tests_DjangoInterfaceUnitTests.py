from django.test import TestCase
from Final.models import User
from Final.models import Course
from Final.models import Lab
from Final.DjangoInterface import DjangoInterface

django_interface = DjangoInterface()

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="User1", password="User1pass", permissions="0000",
                            address="User1Address", phonenumber="User1Phone", email="User1Email")
        User.objects.create(username="User2", password="User2pass", permissions="0000",
                            address="User2Address", phonenumber="User2Phone", email="User2Email")
        User.objects.create(username="myTA", password="TApass", permissions="0001",
                            address="TAAddress", phonenumber="TAPhone", email="TAEmail")
        Course.objects.create(courseId="Course1", instructor="Instructor1", startTime="1PM", endTime="2PM")

    def test_CreateUser(self):
        django_interface.create_user("Test1", "Password1", "0001", "testaddress", "testPhone", "testEmail")
        U = User.objects.get(username="Test1")
        self.assertEquals(User.UsertoStr(U), "User: Test1 Password1 0001 testaddress testPhone testEmail")
        print(User.UsertoStr(U))

    def test_DeleteUser(self):
        U = User.objects.get(username="User1")
        django_interface.delete_user("User1")
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="User1")

    def test_UpdateUser(self):
        django_interface.update_user("User1", "password", "UpdatedPassword")
        django_interface.update_user("User1", "permissions", "1111")
        django_interface.update_user("User1", "address", "UpdatedAddress")
        django_interface.update_user("User1", "phonenumber", "updatedPhone")
        django_interface.update_user("User1", "email", "updatedEmail")
        django_interface.update_user("User1", "username", "UpdatedUsername")
        user1 = User.objects.get(username="UpdatedUsername")
        self.assertEqual(user1.password, "UpdatedPassword")
        self.assertEqual(user1.permissions, "1111")
        self.assertEqual(user1.address, "UpdatedAddress")
        self.assertEqual(user1.phonenumber, "updatedPhone")
        self.assertEqual(user1.email, "updatedEmail")
        self.assertEqual(user1.username, "UpdatedUsername")

    def test_AddUserToCourse(self):
        django_interface.add_user_to_course("Course1", "User1")
        U = User.objects.get(students__studentsInCourse=1)    #based on integer index in list, not the "Username" string
        self.assertEqual(User.objects.get(username="User1"), U)

        U2 = User.objects.get(username="User2")
        c = Course.objects.get(courseId="Course1")
        self.assertNotEqual(c.studentsInCourse.filter(username="User2"), U2)
        #with self.assertRaises(User.DoesNotExist):
        #    User.objects.get(course__students=2)    #This should return an error, as we're trying to grab a user
                                                    #that's not in the database (only 1 in the database right now)
    def test_AddTAToCourse(self):
        django_interface.add_TA_to_course("Course1", "myTA")
        U = User.objects.get(TAs__TAsInCourse__username="myTA")     #funky syntax, using related_name to differentiate
        self.assertEqual(User.objects.get(username="myTA"), U)

        #Trying to get a user who is not in the TAsInCourse list.
        U2 = User.objects.get(username="User1")
        c = Course.objects.get(courseId="Course1")
        self.assertNotEqual(c.TAsInCourse.filter(username="User2"), U2)

    def test_get_all_courses_only_one_course(self):
        courses = django_interface.get_all_courses()
        self.assertEqual(1, len(courses))

    def test_add_two_courses_get_three(self):
        Course.objects.create(courseId="Course2", instructor="Instructor1", startTime="1PM", endTime="2PM")
        Course.objects.create(courseId="Course3", instructor="Instructor1", startTime="1PM", endTime="2PM")
        courses = django_interface.get_all_courses()
        self.assertEqual(3, len(courses))
        django_interface.delete_course("Course2")
        django_interface.delete_course("Course3")

    def test_CreateLab(self):
        django_interface.create_lab(self, "123", "myTA", "1PM", "2PM")
        l = Lab.objects.get(labNumber="123")
        self.assertEquals(l.LabtoStr(), "Lab: 123 myTA 1PM 2PM None")
        print(l.LabtoStr)

    def test_DeleteLab(self):
        django_interface.delete_lab(self, "001")
        with self.assertRaises(Lab.DoesNotExist):
            l = Lab.objects.get(labNumber="001")

    def test_AddStudentToLab(self):
        django_interface.add_student_to_lab(self, "001", "User1")
        myLab = Lab.objects.get(labNumber="001")
        U2 = User.objects.get(username="User2")
        qs = myLab.studentsInLab.filter(username="User1")   #funky queryset notation

        self.assertEqual(1, myLab.studentsInLab.count())
        self.assertEqual(User.objects.get(username="User1"), qs[0])
        self.assertNotEqual(myLab.studentsInLab.filter(username="User2"), U2)

    def test_AddLabSectionsToCourse(self):
        django_interface.add_lab_section_to_course(self, "002", "Course1")
        myLab = Lab.objects.get(labNumber='002')
        myCourse = Course.objects.get(courseId='Course1')
        self.assertEqual(myLab.ParentCourse, myCourse)
        self.assertNotEqual(myLab.ParentCourse, Course.objects.get(courseId="Course2"))

        self.assertEqual("Lab section already has a parent course",
        django_interface.add_lab_section_to_course(self, "002", "Course1")) #acceptance test, move later dumbass