from App import App
from Login import Login
from UserEdits import UserEdits

def main():
    command_string = "true"
    print("True")
    a = App(Login(), UserEdits())
    while command_string != "quit":
        command_string = input("Please enter command: ")
        print(a.command(command_string))


if __name__ == '__main__':
    main().run()
