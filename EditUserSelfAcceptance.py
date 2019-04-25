from django.test import TestCase
from Final.models import User
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
        sessionStudent['permissions'] = '0000'
        sessionStudent.save()

    def test_editUserSelf_isaccessible(self):
        response = self.client1.get('/edituserself/')
        self.assertEqual(response.status_code, 200)

    def test_editUserSelf_noUserSession_redirect(self):
        response = self.clientNoUser.post('/edituserself/', data={'password': 'p'})
        self.assertRedirects(response, '/loginpage/')

    def test_editUserSelf_redirect_successful(self):
        response = self.clientStudent.post('/edituserself/',
                                           data={'password': 'newPass', 'email': '', 'permissions': '', 'address': '',
                                                 'phonenumber': ''})
        self.assertTemplateUsed(template_name='landingpage.html')
