from django.shortcuts import render
from django.http import HttpResponse
from Final.models import MyModel
from Final.forms import CommandForm


# Create your views here.
def index(request):
    myQuery = MyModel.objects.all()
    context = {'myObjects': myQuery}
    return render(request, "index.html", context)

def command(request):
    inputCommand = ""

    if request.method == "POST":
        #Get the input command from the posted form
        InputCommandForm = CommandForm(request.POST)

        if InputCommandForm.is_valid():
            InputCommand = InputCommandForm.cleaned_data['command']
            #do we call App(InputCommand) here?
    else:
        InputCommandForm = CommandForm()

    return render(request, 'command.html', {"command": command})