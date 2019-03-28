from django.shortcuts import render
from django.http import HttpResponse
from Final.models import MyModel


# Create your views here.
def index(request):
    myQuery = MyModel.objects.all()
    context = {'myObjects': myQuery}
    return render(request, "index.html", context)
