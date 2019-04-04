class App:

    def __init__(self, login, user_edits, course_edits):
        self.login = login
        self.userEdits = user_edits
        self.course_edits = course_edits

    def command(self, command_string):
        command_array = command_string.split()
        user = None
        if command_array[0] == "login":
            if user is not None:
                return "User already logged in"
            if len(command_array) != 3:
                return "Invalid parameters for this command"
            user = self.login.login_to_database(command_array[1], command_array[2])
            if user is None:
                return "User does not exist"
        elif command_array[0] == "logout":
            if user is None:
                return "User is not logged in"
            user = self.login.logout(user)
            if user is not None:
                return "Logout was unsuccessful"
            else:
                return "User logged out"
        elif command_array[0] == "add_user":
            if user is None:
                return "User is not logged in"
            if len(command_array) != 3:
                return "Invalid parameters for this command"
            return self.userEdits.add_user(command_array[1], command_array[2], user)
        elif command_array[0] == "delete_user":
            if user is None:
                return "User is not logged in"
            if len(command_array) != 2:
                return "Invalid parameters for this command"
            return self.userEdits.delete_user(command_array[1], user)
        elif command_array[0] == "create_course":
            if user is None:
                return "User is not logged in"
            if len(command_array) != 4:
                return "Invalid parameters for this command"
        else:
            return "This command does not exist"
