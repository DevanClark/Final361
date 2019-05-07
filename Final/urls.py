from django.urls import path
from . import views
from Final.views import *
from django.conf.urls import url

urlpatterns = [
    path('command/', views.command),
    url(r'loginpage/', LoginClass.as_view(), name="loginpage"),
    url(r'landingpage/', views.landingPage, name="landingpage"),
    url('editUserAdmin/', EditUserAdmin.as_view(), name="edituseradmin"),
    url(r'logout', views.Logout, name='logout'),
    url(r'createuser/', views.CreateUserClass.as_view(), name="createuser"),
    url(r'edituserself/', views.EditUserSelfClass.as_view(), name = "edituserself"),
    url(r'createcourse/', CreateCourse.as_view(), name="createcourse"),
    url(r'deletecourse/', DeleteCourse.as_view(), name="deletecourse"),
    url(r'addusertocourse/', AddUserToCourse.as_view(), name="addusertocourse"),
    url(r'deleteuser/', DeleteUser.as_view(), name="deleteuser"),
    url(r'addtatocourse/', AddTaToCourse.as_view(), name="addtatocourse"),
    url(r'viewcourseinfoinstructor', ViewCourseInfoInstructor.as_view(), name="viewcourseinfoinstructor"),
    url(r'edituseradminuserprofile', EditUserAdminUserProfile.as_view(), name='edituseradminuserprofile'),
    url(r'viewcourseinfota', ViewCourseInfoInstructor.as_view(), name="viewcourseinfota")
    # the path for command view
    # add the path to command_result?
    # path ('command_result', views.command_result)
]
