from django.test import TestCase
from Final.models import User
from Final.models import Course
from django.test import Client


class TestCourseInfo(TestCase):

    def setUp(self):
        User.objects.create(username="testInstructor", password="testPassword", permissions="1111",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="TAUsername", password="testPassword", permissions="0001",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="student", password="testPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        Course.objects.create(instructor="testInstructor", courseId="testCourse", startTime="1pm", endTime="2pm")

        self.ta = Client()
        session_ta = self.ta.session
        session_ta['user'] = 'ta'
        self.client1 = Client()
        session_instructor = self.client1.session
        session_instructor['user'] = 'testInstructor'
        session_instructor.save()

        self.clientStudent = Client()
        session_student = self.clientStudent.session
        session_student['user'] = 'student'
        session_student.save()

    def test_view_course_info_all_page_is_accessible(self):
        response = self.client1.get('/viewcourseinfo/')
        self.assertEqual(response.status_code, 200)

    def test_view_course_info_ta_page_is_unaccessbile(self):
        response = self.ta.get('/viewcourseinfota/')
        self.assertEqual(response.status_code, 302)

    def test_view_course_info_superadmin_page_is_unaccessbile(self):
        response = self.client.get('/viewcourseinfosuperadmin/')
        self.assertEqual(response.status_code, 302)




