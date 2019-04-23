class App:

    def __init__(self, login, user_edits, course_edits):
        self.login = login
        self.userEdits = user_edits
        self.course_edits = course_edits
        self.user = None

    def command(self, command_string):
        command_array = command_string.split()
        print("From app:" + command_string)

        if command_array[0] == "login":
            if self.user is not None:
                return "User already logged in"
            if len(command_array) != 3:
                return "Invalid parameters for this command"
            self.user = self.login.login_to_database(command_array[1], command_array[2])
            if self.user is None:
                return "User does not exist"
            if self.user.password != command_array[2]:
                self.user = None
                return "Incorrect username/password"
            return "User logged in"

        elif command_array[0] == "logout":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 1:
                return "Invalid parameters for this command"
            self.user = self.login.logout()
            if self.user is not None:
                return "Logout was unsuccessful"
            else:
                return "User logged out"

        elif command_array[0] == "add_user":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 4:
                return "Invalid parameters for this command"
            return self.userEdits.add_user(command_array[1], command_array[2], command_array[3], self.user)

        elif command_array[0] == "delete_user":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 2:
                return "Invalid parameters for this command"
            return self.userEdits.delete_user(command_array[1], self.user)

        elif command_array[0] == "change_contact":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 4:
                return "Invalid parameters for this command"
            return self.userEdits.change_contact(command_array[1], command_array[2], command_array[3])

        elif command_array[0] == "edit_user":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 4:
                return "Invalid parameters for this command"
            return self.userEdits.edit_user(command_array[1], command_array[2], command_array[3], self.user)

        elif command_array[0] == "create_course":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 5: #Have to change when TAs and lab sections are implemented.
                return "Invalid parameters for this command"
            return self.course_edits.create_course(command_array[1], command_array[2], command_array[3], command_array[4], self.user)

        elif command_array[0] == "delete_course":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 2:
                return "Invalid parameters for this command"
            return self.course_edits.delete_course(command_array[1], self.user)

        elif command_array[0] == "add_user_to_course":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 3:
                return "Invalid parameters for this command"
            return self.course_edits.add_user_to_course(command_array[1], command_array[2], self.user)

        elif command_array[0] == "add_TA_to_course":
            if self.user is None:
                return "User is not logged in"
            if len(command_array) != 3:
                return "Invalid parameters for this command"
            return self.course_edits.add_TA_to_course(command_array[1], command_array[2], self.user)
        else:
            return "This command does not exist"

