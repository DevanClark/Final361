from django.urls import path
from . import views
from Final.views import LoginClass

urlpatterns = [
    path('command/', views.command),
    path('loginpage/', LoginClass.as_view())
    # the path for command view
    # add the path to command_result?
    # path ('command_result', views.command_result)
]
