from App import App
from Login import Login
from UserEdits import UserEdits
from CourseEdit import CourseEdit
from Final.DjangoInterface import DjangoInterface


def main():
    command_string = "true"
    print("True")
    a = App(Login(DjangoInterface()), UserEdits(), CourseEdit())
    while command_string != "quit":
        command_string = input("Please enter command: ")
        print(a.command(command_string))


if __name__ == '__main__':
    main().run()
