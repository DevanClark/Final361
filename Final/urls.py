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
    url(r'assigninstructortocourse', AssignInstructorToCourse.as_view(), name="assigninstructortocourse"),
    url(r'deleteuser/', DeleteUser.as_view(), name="deleteuser"),
    url(r'addtatocourse/', AddTaToCourse.as_view(), name="addtatocourse"),
    url(r'createlab/', CreateLab.as_view(), name="createlab"),
    url(r'deletelab/', DeleteLab.as_view(), name="deletelab"),
    url(r'addstudenttolab', AddStudentToLab.as_view(), name="addstudenttolab"),
    url(r'addlabsectiontocourse', AddLabSectionToCourse.as_view(), name="addlabsectiontocourse"),
    url(r'assigntatolab', AssignTAToLab.as_view(), name="assigntatolab"),
    url(r'addtatocourse/', AddTaToCourse.as_view(), name="addtatocourse"),
    url(r'viewcourseinfo', ViewCourseInfo.as_view(), name="viewcourseinfo"),
    url(r'edituseradminuserprofile', EditUserAdminUserProfile.as_view(), name='edituseradminuserprofile'),
    url(r'viewcourseinfota', ViewCourseInfo.as_view(), name="viewcourseinfota"),
    url(r'viewcourseinfosuperadim', ViewCourseInfo.as_view(), name="viewcourseinfosuperadmin"),
    url(r'viewcontactinfo', ViewContactInfoClass.as_view(), name ="viewcontactinfo")
    # the path for command view
    # add the path to command_result?
    # path ('command_result', views.command_result)
]
