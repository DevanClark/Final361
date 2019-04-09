from django.test import TestCase

# Create your tests here.
from Final.models import User
from Final import DjangoInterface

class UserTestCase(TestCase):
    def setUp(self):
        #Probably need to mess around with how we're storing Permissions and Phone Numbers
        User.objects.create(username="User1", password="User1pass", permissions="0000",
                            address="User1Address", phonenumber="User1Phone", email="User1Email")

    def test_CreateUser(self):
        DjangoInterface.DjangoInterface.create_user(self, "Test1", "Password1")
        U = User.objects.get(username="Test1")
        self.assertEquals(User.UsertoStr(U), "User: Test1 Password1 1ajfjas testaddress stupid testuser")
        print(User.UsertoStr(U))

    def test_DeleteUser(self):
        U = User.objects.get(username="User1")
        TF = User.objects.exists(U)
        print(TF)
        DjangoInterface.DjangoInterface.delete_user(self, "User1")

        #U = User.objects.get(username="User1") #Test errors out with this in.
        #print("This shouldn't print anything:" + User.UsertoStr(U))

    def test_UpdateUser(self):
        U = User.objects.get(username="User1")
        print("U before updating its fields with DjangoInterface " + User.UsertoStr(U))
        DjangoInterface.DjangoInterface.update_user(self, "User1", "password", "UpdatedPassword")
        DjangoInterface.DjangoInterface.update_user(self, "User1", "permissions", "UpdatedPermissions")
        DjangoInterface.DjangoInterface.update_user(self, "User1", "address", "UpdatedAddress")
        DjangoInterface.DjangoInterface.update_user(self, "User1", "phonenumber", "updatedPhone")
        DjangoInterface.DjangoInterface.update_user(self, "User1", "email", "updatedEmail")
        DjangoInterface.DjangoInterface.update_user(self, "User1", "username", "UpdatedUsername")

        U2 = User.objects.get(username="UpdatedUsername")
        print("U after updating its fields with DjangoInterface " + User.UsertoStr(U2))

    def test_RemoveLater(self):
        myUser = User.objects.get(username="User1")
        #myUser = User.objects.get(password="User1pass")
        print(myUser.username)
        print(myUser.password)

        #testUser.create_user(self, "test", "testpass")

        print("work:" + User.UsertoStr(myUser))
