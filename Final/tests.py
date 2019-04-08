from django.test import TestCase

# Create your tests here.
from Final.models import User
from Final import DjangoInterface

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="User1", password="User1pass")

    def TestCreateUser(self):
        UsernameP = "test11"
        PasswordP = "password11"
        DjangoInterface.DjangoInterface.create_user(self, UsernameP, PasswordP)
        U = User.objects.get(username=UsernameP)
        print("DjangoInterface test: " + User.UsertoStr(U))

        UsernameP2 = "DNE"
        U2 = User.objects.get(username=UsernameP2)
        User.UsertoStr(U2)
        #TestCase.assertEquals(self, User.UsertoStr(U2), )

    def TestDeleteUser(self):
        DjangoInterface.DjangoInterface.delete_user(self, UsernameP)
      #  U = User.objects.get(username=UsernameP) Test errors out with this in.
        print("This shouldn't [print anything:" + User.UsertoStr(U))

    def TestUpdateUser(self):
        test = "test"

    def TestMisc(self):
        myUser = User.objects.get(username="User1")
        #myUser = User.objects.get(password="User1pass")
        print(myUser.username)
        print(myUser.password)

        #testUser.create_user(self, "test", "testpass")

        print("work:" + User.UsertoStr(myUser))
