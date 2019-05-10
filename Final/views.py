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
from LabEdit import LabEdit
from DataRetrieval import DataRetrieval
from Final.DjangoInterface import DjangoInterface

a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
l = Login(DjangoInterface())
c = CourseEdit()
u = UserEdits()
la = LabEdit()
d = DjangoInterface()
dr = DataRetrieval()
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


class ViewCourseInfo(View):
    def get(self, request):
        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')

        if user.permissions[0] == "1" or user.permissions[1] == "1":
            all_users = dr.view_database(user)
            all_courses = dr.get_all_courses(user)
            all_labs = dr.get_all_labs(user)
            return render(request, 'main/viewcourseinfosuperadmin.html', {'all_courses': all_courses, 'all_users':all_users, 'all_labs':all_labs})

        if user.permissions[2] == "1":
            courses = dr.get_classes_by_instructor(user)
            ta_courses = dr.get_ta_assignments(user)
            return render(request, 'main/viewcourseinfo.html', {'courses': courses, 'ta_courses': ta_courses})
        if user.permissions[3] == "1":
            courses_for_one_ta = dr.get_classes_by_ta(user)
            return render(request, 'main/viewcourseinfota.html', {'ta_courses': courses_for_one_ta})


class EditUserAdminUserProfile(View):
    def get(self, request):
        user_to_edit = User.objects.get(username=request.session['user_to_edit'])
        data = {
            'username': user_to_edit.username,
            'password': user_to_edit.password,
            'superPermission': int(user_to_edit.permissions[0]),
            'adminPermission': int(user_to_edit.permissions[1]),
            'instructorPermission': int(user_to_edit.permissions[2]),
            'taPermission': int(user_to_edit.permissions[3]),
            'address': user_to_edit.address,
            'email': user_to_edit.email,
            'phonenumber': user_to_edit.phonenumber
        }
        form = EditUserForm(data)
        return render(request, 'main/edituseradminuserprofile.html', {'form': form})

    def post(self, request):
        if request.method == "POST":
            user_to_edit = User.objects.get(username=request.session['user_to_edit'])
            permissions = user_to_edit.permissions
            data = {
                'username': user_to_edit.username,
                'password': user_to_edit.password,
                'superPermission': int(user_to_edit.permissions[0]),
                'adminPermission': int(user_to_edit.permissions[1]),
                'instructorPermission': int(user_to_edit.permissions[2]),
                'taPermission': int(user_to_edit.permissions[3]),
                'address': user_to_edit.address,
                'email': user_to_edit.email,
                'phonenumber': user_to_edit.phonenumber
            }
            form = EditUserForm(request.POST, initial=data)
            if form.has_changed():
                for value in form.changed_data:
                    if "Permission" not in value and value is not "username":
                        d.update_user(user_to_edit.username, value, form.data[value])
                    else:
                        if value is "superPermission":
                            if permissions[0] == '0':
                                permissions = "1" + permissions[1:]
                            else:
                                permissions = "0" + permissions[1:]
                        if value is "adminPermission":
                            if permissions[1] == '0':
                                permissions = permissions[0] + "1" + permissions[2:]
                            else:
                                permissions = permissions[0] + "0" + permissions[2:]
                        if value is "instructorPermission":
                            if permissions[2] == '0':
                                permissions = permissions[0:2] + "1" + permissions[3:]
                            else:
                                permissions = permissions[0:2] + "0" + permissions[3:]
                        if value is "taPermission":
                            if permissions[3] == '0':
                                permissions = permissions[0:3] + "1"
                            else:
                                permissions = permissions[0:3] + "0"
                        d.update_user(user_to_edit.username, "permissions", permissions)
            return redirect('edituseradmin')


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
        if request.POST['user_to_edit'] == "":
            return render(request, 'main/editUserAdmin.html',
                          {"edituseradminresponse": "Have to add the user field to change their information"})
        try:
            user_to_edit = User.objects.get(username=request.POST['user_to_edit'])
        except Exception as e:
            return render(request, 'main/editUserAdmin.html', {"edituseradminresponse": "User does not exist"})
        request.session['user_to_edit'] = user_to_edit.username
        return redirect('edituseradminuserprofile')

class CreateLab(View):
    def get(self, request):
        return render(request, 'main/createlab.html')

    def post(self, request):
        print(request.session.get('user'))

        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')

        val = la.create_lab(request.POST["TA"], request.POST["labNumber"], request.POST["starttime"], request.POST["endtime"], user)
        return render(request, 'main/createlab.html', {"createlabreponse": val})



class DeleteLab(View):
    def get(self, request):
        return render(request, 'main/deletelab.html')

    def post(self, request):
        print(request.session.get('user'))

        try:
            user = User.objects.get(username=request.session.get('user'))
        except Exception as e:
            return redirect('loginpage')
        val = la.delete_lab(request.POST["labNumber"], user)
        return render(request, 'main/deletelab.html', {"deletelabresponse": val})