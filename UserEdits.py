from Final import DjangoInterface
class UserEdits:

    def __init__(self):
        self = self
#        self.myDj = DjangoInterface()

    def add_user(self, username, password, permissions, loggedinuser):
        if loggedinuser.permissions[0] != 1 or loggedinuser.permissions[1] != 1:
            return "Illegal permissions to do this activity"
        try:
            DjangoInterface.DjangoInterface.create_user(self, username, password)
        except Exception as e:
            print(e)
            return "Error"
        return "User successfully added"  #Whatever was written in the acceptance tests

    def delete_user(self, usertodelete, loggedinuser):
        try:
            DjangoInterface.DjangoInterface.delete_user(self, usertodelete)
        except Exception as e:
            return "Error"
        return "User successfully deleted"

    def change_contact(self, usernameToChange, fieldToChange, updatedInfo, loggedInUser):
        try:
            DjangoInterface.DjangoInterface.update_user(self, usernameToChange, fieldToChange, updatedInfo)
        except Exception as e:
            return "Error"
        return "User updated"

    def edit_user(self, usertoedit, desiredfield, changedfield, loggedinuser):
        return "yes"
