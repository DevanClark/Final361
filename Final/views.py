from django.shortcuts import render
from django.http import HttpResponse
from Final.models import MyModel
from Final.forms import CommandForm
from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit

# Create your views here.
def index(request):
    myQuery = MyModel.objects.all()
    context = {'myObjects': myQuery}
    return render(request, "index.html", context)


def command(request):
    inputCommand = ""

    if request.method == "POST":
        # Get the input command from the posted form
        InputCommandForm = CommandForm(request.POST)

        if InputCommandForm.is_valid():
            InputCommand = InputCommandForm.cleaned_data['command']
            print(InputCommand)
            # do we call App(InputCommand) here?
            a = App(Login(), UserEdits(), CourseEdit())
            print(a.command(str(InputCommand)))
    else:
        InputCommandForm = CommandForm()

    return render(request, 'commandForm.html', {"command": command})
