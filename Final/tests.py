from django.test import TestCase

# Create your tests here.
from Final.models import User
from Final import DjangoInterface

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test", password="testpass")

    def testingAccountCreation(self):
        testUser = DjangoInterface()

        myUser = User.objects.get(username="test")
        myUser = User.objects.get(password="testpass")

        testUser.create_user(self, "test", "testpass")

        print("work:" + User.UsertoStr(test))