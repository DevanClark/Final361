from django.urls import path
from . import views
from Final.views import LoginClass
from django.conf.urls import url
urlpatterns = [
    path('command/', views.command),
    url(r'loginpage/', LoginClass.as_view(), name="loginpage"),
    path(r'landingpage/', views.landingPage, name="landingpage"),
    path('editUserAdmin/', views.edituserAdmin),
    url(r'logout', views.Logout, name='logout')
    path('loginpage/', LoginClass.as_view()),
    path('landingpage/', views.command),
    path('createuser/', views.CreateUserClass.as_view()),
    path('edituserself/', views.EditUserSelfClass.as_view()),
    # the path for command view
    # add the path to command_result?
    # path ('command_result', views.command_result)
]
