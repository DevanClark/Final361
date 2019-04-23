from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from Final.models import MyModel
from Final.forms import CommandForm
from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Final.DjangoInterface import DjangoInterface

a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
l = Login(DjangoInterface())

# Create your views here.


def command(request):
    inputCommand = ""
    cmdResponse = ""

    if request.method == "POST":
        # Get the input command from the posted form
        InputCommandForm = CommandForm(request.POST)

        if InputCommandForm.is_valid():
            InputCommand = InputCommandForm.cleaned_data['command']
            cmdResponse = a.command(str(InputCommand))
    else:
        InputCommandForm = CommandForm()

    return render(request, 'commandForm.html', {"cmdResponse": cmdResponse})


class LoginClass(View):
    def get(self, request):
        return render(request, 'main/loginpage.html')

    def post(self, request):
        stringOut = " "
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        self.user = l.login_to_database(username, password)
        if self.user is None:
            loginReponse = "Username or password is incorrect. Please try again!"
            return render(request, 'main/loginpage.html', {"loginResponse": loginReponse})
        else:
            return render(request, 'main/landingpage.html')


class EditUserSelfClass(View):
    def get(self, request):
        return render(request, 'main/edituserself.html')

    def post(self, request):
        stringOut = " "
        print(request.POST)
        if request.POST["password"] is not None:
            password = request.POST["password"]
            self.user = self.user.edit_user(self.user, "password", password, self.user)

        if request.POST["email"] is not None:
            email = request.POST["email"]
            self.user = self.user.edit_user(self.user, "email", email, self.user)

        if request.POST["permissions"] is None:
            permissions = request.POST["permissions"]
            self.user = self.user.edit_user(self.user, "permissions", permissions, self.user)

        if request.POST["address"] is None:
            address = request.POST["address"]
            self.user = self.user.edit_user(self.user, "address", address, self.user)

        if request.POST["phonenumber"] is None:
            phonenumber = request.POST["phonenumber"]
            self.user = self.user.edit_user(self.user, "phonenumber", phonenumber, self.user)

        if self.user is None:
            editUserSelfResponse = "Invalid information. Please try again!"
            return render(request, 'main/edituserself.html', {"editUserSelfResponse": editUserSelfResponse})
        else:
            return render(request, 'main/landingpage.html')


class CreateUserClass(View):
    def get(self, request):
        return render(request, 'main/createuser.html')

    def post(self, request):
        stringOut = " "
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        permissions = request.POST["permissions"]
        address = request.POST["address"]
        phonenumber = request.POST["phonenumber"]
        newUser = self.user.create_user(username, password, permissions, phonenumber, address, email)
        if newUser is None:
            createUserResponse = "Invalid information. Please try again!"
            return render(request, 'main/createuser.html', {"createUserResponse": createUserResponse})
        else:
            return render(request, 'main/landingpage.html')