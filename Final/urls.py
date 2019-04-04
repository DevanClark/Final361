from django.urls import path
from . import views

urlpatterns = [
    path('command/', views.command),
    # the path for command view
    # add the path to command_result?
    # path ('command_result', views.command_result)
]
