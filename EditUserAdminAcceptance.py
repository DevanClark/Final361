from django.test import TestCase
from App import App
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Login import Login
from Final.DjangoInterface import DjangoInterface
from Final.models import User
from Final.models import Course

from django.test import Client
from django.test.utils import setup_test_environment



class TestApp(TestCase):

    def setUp(self):
        # Setting up mock database
        User.objects.create(username="testUsername", password="testPassword", permissions="1111",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="brokenUsername", password="brokenPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="delUsername", password="delPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")

        self.client1 = Client()
        session = self.client1.session
        session['user'] = 'testUsername'
        session['permissions'] = '0001'
        session.save()

        self.clientNoUser = Client()
        sessionNoUser = self.clientNoUser.session
        sessionNoUser['user'] = ''
        sessionNoUser.save()

        self.clientStudent = Client()
        sessionStudent = self.clientStudent.session
        sessionStudent['user'] = 'delUsername'
        sessionStudent['permissions'] ='0000'
        sessionStudent.save()

    def test_editUserAdmin_isaccessible(self):
        response = self.client1.get('/editUserAdmin/')
        self.assertEqual(response.status_code, 200)

    def test_editUserAdmin_noUserToEdit_unsuccessful(self):
        response = self.client1.post('/editUserAdmin/', data={'usertoedit': ''})
        str = 'Have to add the user field to change their information'
        self.assertEqual(response.context['edituseradminresponse'], str)

    def test_editUserAdmin_noUserSession_redirect(self):
        response = self.clientNoUser.post('/editUserAdmin/', data={'usertoedit': 'u', 'password':'p'})
        self.assertRedirects(response, '/loginpage/')

    def test_editUserAdmin_successful(self):
        response = self.client1.post('/editUserAdmin/', data={'usertoedit': 'testUsername', "password": 'newPass'})
        str = 'User successfully updated'
        self.assertEqual(response.context['edituseradminresponse'], str)

    def test_editUserAdmin_illegalUserPermission_unsuccessful(self):
        response = self.clientStudent.post('/editUserAdmin/', data={'usertoedit': 'testUsernam', "password": 'newPass'})
        str = 'Illegal permissions to do this action'
        self.assertEqual(response.context['edituseradminresponse'], str)



