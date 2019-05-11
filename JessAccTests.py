from django.test import TestCase
from Final.DjangoInterface import DjangoInterface
from Final.models import User
from django.test import Client


class TestApp(TestCase):

    def setUp(self):
        # Setting up mock database
        User.objects.create(username="testUsername", password="testPassword", permissions="1111",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")
        User.objects.create(username="brokenUsername", password="brokenPassword", permissions="0000",
                            address="testAddress", phonenumber="TestPhoneNum", email="TestEmail")

        self.client1 = Client()
        session = self.client1.session
        session['user'] = 'testUsername'
        session['permissions'] = '0001'
        session.save()

        self.clientNoUser = Client()
        sessionNoUser = self.clientNoUser.session
        sessionNoUser.save()

        self.clientBad = Client()
        sessionBad = self.clientBad.session
        sessionBad['user'] = 'brokenUsername'
        sessionBad['permissions'] = '0000'
        sessionBad.save()

    def test_editUserSelf_isaccessible(self):
        response = self.client1.get('/createcourse/')
        self.assertEqual(response.status_code, 200)

    def test_create_user_improper_parameters_password_too_small(self):
        response1 = self.client1.post('/createuser/', data={'username': 'u', 'password': 'p', 'email': 'e@aol.net',
                                                           'supervisorbox': '1', 'address': 'a',
                                                           'phonenumber': 'test'})
        str1 = "Failed to add user. Improper parameters"
        self.assertEqual(response1.context["createUserResponse"], str1)

    def test_create_user_pass(self):
        response1 = self.client1.post('/createuser/', data={'username': 'u', 'password': 'password', 'email': 'e@aol.net',
                                                                'supervisorbox': '1', 'address': 'a',
                                                                'phonenumber': 'test'})
        str1 = "User successfully added"
        self.assertEqual(response1.context["createUserResponse"], str1)

    def test_createuser2(self):
        response2 = self.clientBad.post('/createuser/', data={'username': '', 'password': '', 'email': '',
                                                            'permissions': '', 'address': '', 'phonenumber': ''})
        str2 = "Illegal permissions to do this action"
        self.assertEqual(response2.context["createUserResponse"], str2)

    def test_createcourse(self):
        response1 = self.client1.post('/createcourse/', data={'instructor': 'testUsername', 'coursename': 'p',
                                                              'starttime': '8:00', 'endtime': '12:00'})
        str1 = "Course successfully added"
        self.assertEqual(response1.context["createcoursereponse"], str1)

        response2 = self.clientNoUser.post('/createcourse/', data={'instructor': 'beep', 'coursename': '', 'starttime': '',
                                                             'endtime': ''})
        self.assertRedirects(response2, '/loginpage/')

    def test_view_contact_info(self):
        response1 = self.clientNoUser.get('/viewcontactinfo/')
        self.assertRedirects(response1, '/loginpage/')

    def test_no_permissions(self):
        response2 = self.clientBad.get('/viewcontactinfo/')
        self.assertRedirects(response2, '/landingpage/')