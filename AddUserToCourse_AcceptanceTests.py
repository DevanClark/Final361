from django.test import TestCase
from Final.models import User
from Final.models import Course
from django.test.client import RequestFactory
from django.test import Client
from django.test.utils import setup_test_environment


class AddUserToCourseAcceptanceTests(TestCase):

    def setUp(self):
        # Setting up mock database
        self.test_user = User.objects.create(username="testUsername", password="testPassword", permissions="1111",
                                             address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="brokenUsername", password="brokenPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="delUsername", password="delPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        self.test_super = User.objects.create(username="testSuper", password="testPassword", permissions="1000",
                                              address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        self.test_admin = User.objects.create(username="testAdmin", password="testPassword",
                                              permissions="0100",
                                              address="testAddress", phonenumber="TestPhoneNum",
                                              email="TestEmail")
        self.test_instructor = User.objects.create(username="testInstructor", password="testPassword",
                                                   permissions="0010",
                                                   address="testAddress", phonenumber="TestPhoneNum",
                                                   email="TestEmail")
        self.test_user = User.objects.create(username="testUser", password="testPassword",
                                             permissions="0000",
                                             address="testAddress", phonenumber="TestPhoneNum",
                                             email="TestEmail")
        self.client = Client()
        self.client1 = Client()
        self.factory = RequestFactory()
        Course.objects.create(instructor="testInstructor", courseId="testCourse", startTime="1pm", endTime="2pm")
        User.objects.create(username="TAUsername", password="testPassword", permissions="0001",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")

    def test_add_user_to_course_page_is_accessible(self):
        response = self.client.get('/addusertocourse/')
        self.assertEqual(response.status_code, 200)

    def test_add_user_no_logged_in_user_redirect_landing_page(self):
        r = self.client.post('/addusertocourse/', data={'courseid': 'testCourse', 'usertoadd': 'test'})
        self.assertRedirects(r, '/loginpage/')

    def test_add_user_succeeds(self):
        session = self.client.session
        session['user'] = 'testUsername'
        session['permissions'] = '1111'
        session.save()
        response = self.client.post('/addusertocourse/', data={'courseid': 'testCourse', 'usertoadd': 'testUser'})
        str = 'User successfully added to course'
        self.assertEqual(response.context['addusertocourseresponse'], str)

    def test_add_user_class_does_not_exist(self):
        session = self.client.session
        session['user'] = 'testUsername'
        session['permissions'] = '1111'
        session.save()
        response = self.client.post('/addusertocourse/', data={'courseid': 'd', 'usertoadd': 'testUser'})
        str = 'Failed to add user to course.'
        self.assertEqual(response.context['addusertocourseresponse'], str)

    def test_add_ta_user_does_not_exist(self):
        session = self.client.session
        session['user'] = 'testUsername'
        session['permissions'] = '1111'
        session.save()
        response = self.client.post('/addusertocourse/', data={'courseid': 'testCourse', 'usertoadd': 't'})
        str = 'Failed to add user to course.'
        self.assertEqual(response.context['addusertocourseresponse'], str)

    def test_add_user_do_not_have_permission(self):
        session = self.client.session
        session['user'] = 'testUser'
        session.save()
        response = self.client.post('/addusertocourse/', data={'courseid': 'testCourse', 'usertoadd': 'testUsername'})
        str = 'Illegal permissions to do this action'
        self.assertEqual(response.context['addusertocourseresponse'], str)
