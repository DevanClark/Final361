from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Final.DjangoInterface import DjangoInterface
from django.conf import settings

def test():
    command_string = "true"
    print("True")
    a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
    while command_string != "quit":
        command_string = input("Please enter command: ")
        print(a.command(command_string))


if __name__ == '__test__':
    import django
    django.setup()
    test().run()
