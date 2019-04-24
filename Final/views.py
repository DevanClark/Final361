from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from Final.models import MyModel
from Final.models import User
from Final.forms import *
from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Final.DjangoInterface import DjangoInterface

a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
l = Login(DjangoInterface())


ue = UserEdits()
# Create your views here.



def index(request):
    myQuery = MyModel.objects.all()
    context = {'myObjects': myQuery}
    return render(request, "index.html", context)


def command(request):
    inputCommand = ""
    cmdResponse = ""

    if request.method == "POST":
        # Get the input command from the posted form
        InputCommandForm = CommandForm(request.POST)

        if InputCommandForm.is_valid():
            InputCommand = InputCommandForm.cleaned_data['command']
            print(a.command(str(InputCommand)))
            cmdResponse = a.command(str(InputCommand))
    else:
        InputCommandForm = CommandForm()

    return render(request, 'commandForm.html', {"cmdResponse": cmdResponse})


def landingPage(request):
    return render(request, "main/landingpage.html")

def Logout(request):
    if request.method == "POST":
        try:
            del request.session['user']
        except KeyError:
            pass
        return redirect("loginpage")


class LoginClass(View):
    def get(self, request):
        if not request.session.get("user", ""):
            return render(request, "main/loginpage.html")
        return render(request, 'main/landingpage.html')

    def post(self, request):
        stringOut = " "
        print(request.POST)
        try:
            loggedInUser = User.objects.get(username=request.POST["username"])
        except Exception as e:
            return render(request, 'main/loginpage.html', {"loginResponse": "User does not exist"})

        if loggedInUser.password != request.POST["password"]:
            return render(request, 'main/loginpage.html', {"loginResponse": "Username or password is incorrect"})

        request.session['user'] = loggedInUser.username
        return redirect('landingpage')



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


def edituserAdmin(request):

    if request.method == "POST":
        loggedInUser = User.objects.get(username=request.session["user"])
        if request.POST['usertoedit'] is None:
            return render('editUserAdmin.html', {"edituserAdminResponse": "Have to add the user field to change their information"})
        for fieldToChange in request.POST:
            if(fieldToChange != 'usertoedit' and request.POST[fieldToChange] != "" and fieldToChange != 'csrfmiddlewaretoken'):
                ue.edit_user(request.POST['usertoedit'], fieldToChange, request.POST[fieldToChange], loggedInUser)
        # for fieldtochange in request.POST.items():
        #     if fieldtochange is not None:
        #         ue.edit_user(request.POST['usertoedit'], fieldtochange, fieldtochange, loggedInUser)
    return render(request, 'editUserAdmin.html')
        # inputEditForm = EditUserForm(request.POST)

        # if inputEditForm.is_valid():
        #
        #     username = inputEditForm.cleaned_data['username']
        #     user = User.objects.get(username=username)
        #
        #     password = inputEditForm.cleaned_data['password']
        #     permissions = inputEditForm.cleaned_data['permissions']
        #
        #     address = inputEditForm.cleaned_data['address']
        #     phonenumber = inputEditForm.cleaned_data['phonenumber']
        #     email = inputEditForm.cleaned_data['email']
        #
        #     #update_user info
        #     ue.edit_user(username, "password", password, user)
        #     ue.edit_user(username, "permissions", permissions, user)
        #     ue.edit_user(username, "address", address, user)
        #     ue.edit_user(username, "phonenumber", phonenumber, user)
        #     ue.edit_user(username, "email", email, user)

    #
    #         return redirect('landingpage')
    #
    # else:
    #     inputEditForm = EditUserForm()
    #
    # return render(request, 'editUserAdmin.html', {'form': inputEditForm})
