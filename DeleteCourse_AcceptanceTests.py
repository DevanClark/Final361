from django.test import TestCase
from Final.models import User
from Final.models import Course
from django.test import Client


class TestDelete(TestCase):

    def setUp(self):
        User.objects.create(username="testInstructor", password="testPassword", permissions="1111",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="TAUsername", password="testPassword", permissions="0001",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")

        User.objects.create(username="student", password="testPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        Course.objects.create(instructor="testInstructor", courseId="testCourse", startTime="1pm", endTime="2pm")

        self.client = Client()
        self.client1 = Client()
        session = self.client1.session
        session['user'] = 'testInstructor'
        session.save()

        self.clientStudent = Client()
        sessionStudent = self.clientStudent.session
        sessionStudent['user'] = 'student'
        sessionStudent.save()

    def test_delete_course_page_is_accessible(self):
        response = self.client.get('/deletecourse/')
        self.assertEqual(response.status_code, 200)

    def test_delete_course_page_is_successful(self):
        response = self.client1.post('/deletecourse/', data={'coursename': 'testCourse'})
        correctStr = 'Course successfully deleted'
        self.assertEqual(response.context['deletecourseresponse'], correctStr)

    def test_delete_course_page_courseDNE(self):
        response = self.client1.post('/deletecourse/', data={'coursename': 'afgaskglfa'})
        correctStr = 'Course unsuccessfully deleted'
        self.assertEqual(response.context['deletecourseresponse'], correctStr)

    def test_delete_course_page_emptyfield(self):
        response = self.client1.post('/deletecourse/', data={'coursename': ''})
        correctStr = 'Course unsuccessfully deleted'
        self.assertEqual(response.context['deletecourseresponse'], correctStr)

    def test_delete_course_page_illegalPermissions(self):
        response = self.clientStudent.post('/deletecourse/', data={'coursename': 'testCourse'})
        correctStr = 'Illegal permissions to do this action'
        self.assertEqual(response.context['deletecourseresponse'], correctStr)
