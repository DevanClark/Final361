from django.shortcuts import render
from django.http import HttpResponse
from Final.models import MyModel
from Final.forms import CommandForm
from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Final.DjangoInterface import DjangoInterface

a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
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
