from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from Final.models import MyModel
from Final.models import User
from Final.models import Course
from Final.forms import *
from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Final.DjangoInterface import DjangoInterface

a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
l = Login(DjangoInterface())
c = CourseEdit()
u = UserEdits()
# Create your views here.


user = None


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
        return redirect('loginpage')


class LoginClass(View):
    def get(self, request):
        if not request.session.get("user", ""):
            return render(request, "main/loginpage.html")
        return redirect('landingpage')

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
        user = loggedInUser
        return redirect('landingpage')


class CreateCourse(View):
    def get(self, request):
        return render(request, 'main/createcourse.html')

    def post(self, request):
        print(request.session.get('user'))

        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')

        val = c.create_course(request.POST["instructor"], request.POST["coursename"], request.POST["starttime"],
                              request.POST["endtime"], user)
        return render(request, 'main/createcourse.html', {"createcoursereponse": val})


class DeleteUser(View):
    def get(self, request):
        return render(request, 'main/deleteuser.html')

    def post(self, request):
        print(request.session.get('user'))

        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')

        val = u.delete_user(request.POST["usertodelete"], user)
        return render(request, 'main/deleteuser.html', {"deleteuserresponse": val})


class DeleteCourse(View):
    def get(self, request):
        return render(request, 'main/deletecourse.html')

    def post(self, request):
        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')
        val = c.delete_course(request.POST["coursename"], user)
        return render(request, 'main/deletecourse.html', {"deletecourseresponse": val})


class AddUserToCourse(View):
    def get(self, request):
        return render(request, 'main/addusertocourse.html')

    def post(self, request):
        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')
        val = c.add_user_to_course(request.POST["courseid"], request.POST["usertoadd"], user)
        return render(request, 'main/addusertocourse.html', {"addusertocourseresponse": val})


class AddTaToCourse(View):
    def get(self, request):
        return render(request, 'main/addtatocourse.html')

    def post(self, request):
        print(request.session.get('user'))

        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')

        val = c.add_TA_to_course(request.POST["courseid"], request.POST["tatoadd"], user)
        return render(request, 'main/addtatocourse.html', {"addtatocourseresponse": val})


class EditUserSelfClass(View):
    def get(self, request):
        return render(request, 'main/edituserself.html')

    def post(self, request):
        stringOut = " "
        response = " "
        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')

        if request.POST["password"] != "":
            password = request.POST["password"]
            response = u.change_contact(user.username, "password", password)

        if request.POST["email"] != "":
            email = request.POST["email"]
            response = u.change_contact(user.username, "email", email)

        if request.POST["permissions"] != "":
            permissions = request.POST["permissions"]
            response = u.change_contact(user.username, "permissions", permissions)

        if request.POST["address"] != "":
            address = request.POST["address"]
            response = u.change_contact(user.username, "address", address)

        if request.POST["phonenumber"] != "":
            phonenumber = request.POST["phonenumber"]
            response = u.change_contact(user.username, "phonenumber", phonenumber)

        if response is None:
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
        address = request.POST["address"]
        phonenumber = request.POST["phonenumber"]

        permissions = "0000"
        if request.POST.get("supervisorbox"):
            permissions[0] = "1" + permissions[1:]
        if request.POST.get("adminbox"):
            permissions = permissions[0] + "1" + permissions[2:]
        if request.POST.get("instructorbox"):
            permissions = permissions[0:2] + "1" + permissions[3:]
        if request.POST.get("tabox"):
            permissions = permissions[0:3] + "1"
        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')
        createUserResponse = u.add_user(username, password, permissions, phonenumber, address, email, user)
        return render(request, 'main/createuser.html', {"createUserResponse": createUserResponse})


class ViewCourseInfoInstructor(View):
    def get(self, request):
        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')

        try:
            courses = Course.objects.filter(instructor=user.username)
        except Exception as e:
            print(e)
            return render(request, 'main/viewcourseinfoinstructor.html',
                          {"viewcourseinforesponse": "No Courses Currently"})

        return render(request, 'main/viewcourseinfoinstructor.html', {'courses': courses})






class EditUserAdmin(View):
    def get(self, request):
        return render(request, 'main/editUserAdmin.html')

    def post(self, request):
        response = None
        if request.method == "POST":
            try:
                loggedInUser = User.objects.get(username=request.session.get('user'))
            except Exception as e:
                return redirect('loginpage')
        if request.POST['usertoedit'] == "":
            return render(request, 'main/editUserAdmin.html',
                          {"edituseradminresponse": "Have to add the user field to change their information"})
        for fieldToChange in request.POST:
            if fieldToChange != 'usertoedit' and request.POST[
                fieldToChange] != "" and fieldToChange != 'csrfmiddlewaretoken':
                response = u.edit_user(request.POST['usertoedit'], fieldToChange, request.POST[fieldToChange],
                                       loggedInUser)
        return render(request, 'main/editUserAdmin.html', {"edituseradminresponse": response})
