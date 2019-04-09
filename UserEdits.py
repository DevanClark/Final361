from Final import DjangoInterface
class UserEdits:

    def __init__(self):
        self = self
#        self.myDj = DjangoInterface()

    def add_user(self, username, password, loggedinuser):
        print("User in Edits: " + username)
        print("Pass in Edits: " + password)
        try:
            DjangoInterface.DjangoInterface.create_user(self, username, password)
        except Exception as e:
            print(e)
            return "Error"
        return "User successfully added"  #Whatever was written in the acceptance tests

    def delete_user(self, usertodelete, loggedinuser):
        try:
            DjangoInterface.DjangoInterface.delete_user(usertodelete)
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
