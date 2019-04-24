from django.urls import path
from . import views
from Final.views import *
from django.conf.urls import url

urlpatterns = [
    path('command/', views.command),
    url(r'loginpage/', LoginClass.as_view(), name="loginpage"),
    url(r'landingpage/', views.landingPage, name="landingpage"),
    url('editUserAdmin/', views.edituserAdmin, name="edituseradmin"),
    url(r'logout', views.Logout, name='logout'),
    url(r'createuser/', views.CreateUserClass.as_view(), name="createuser"),
    url(r'edituserself/', views.EditUserSelfClass.as_view(), name = "edituserself"),
    url(r'createcourse/', CreateCourse.as_view(), name="createcourse"),
    url(r'deletecourse/', DeleteCourse.as_view(), name="deletecourse"),
    url(r'addusertocourse/', AddUserToCourse.as_view(), name="addusertocourse"),
    url(r'deleteuser/', DeleteUser.as_view(), name="deleteuser"),
    url(r'addtatocourse/', AddTaToCourse.as_view(), name="addtatocourse")

    # the path for command view
    # add the path to command_result?
    # path ('command_result', views.command_result)
]
