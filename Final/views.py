from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from Final.models import MyModel
from Final.forms import *
from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Final.DjangoInterface import DjangoInterface

a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
l = Login(DjangoInterface())

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



def edituserAdmin(request):

    if request.method == "POST":
        inputEditForm = EditUserForm(request.POST)

        if inputEditForm.is_valid():
            username = inputEditForm.cleaned_data['username']
            password = inputEditForm.cleaned_data['password']
            permissions = inputEditForm.cleaned_data['permissions']

            address = inputEditForm.cleaned_data['address']
            phonenumber = inputEditForm.cleaned_data['phonenumber']
            email = inputEditForm.cleaned_data['email']
            return HttpResponseRedirect('/thanks!/')

    else:
        inputEditForm = EditUserForm()

    return render(request, 'editUserAdmin.html', {'form': inputEditForm})
