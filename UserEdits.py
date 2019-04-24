from Final import DjangoInterface
from Final.models import *


class UserEdits:

    def __init__(self):
        self = self

    def add_user(self, username, password, permissions, address, phonenumber, email, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        if len(permissions) != 4:
            return "Failed to add user. Improper parameters"
        if not username.strip():  # this equates to if usersame == " "
            return "Failed to add user. Improper parameters"
        if not password.strip():
            return "Failed to add user. Improper parameters"
        if not permissions.strip():
            return "Failed to add user. Improper parameters"
        if '*' in username:
            return "Failed to add user. Improper parameters"
        if not address.strip():
            return "Failed to add user. Improper parameters"
        if not phonenumber.strip():
            return "Failed to add user. Improper parameters"
        if not email.strip():
            return "Failed to add user. Improper parameters"
        if len(password) < 2:
            return "Failed to add user. Improper parameters"
        try:
            DjangoInterface.DjangoInterface.create_user(self, username, password, permissions, address, phonenumber, email)
        except Exception as e:
            print(e)
            return "Failed to add user."
        return "User successfully added"  # Whatever was written in the acceptance tests

    def delete_user(self, usertodelete, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        if usertodelete == logged_in_user.username:
            return "Unable to delete active user"
        try:
            DjangoInterface.DjangoInterface.delete_user(self, usertodelete)
        except Exception as e:
            return "User unsuccessfully deleted"
        return "User successfully deleted"

    def change_contact(self, user_to_change, field_to_change, updated_field):
        if field_to_change == "username":
            return "Invalid parameter for this command"
        all_field_names = User._meta.get_fields()
        for field in all_field_names:
            if not field.is_relation and field_to_change == field.attname:
                try:
                    DjangoInterface.DjangoInterface.update_user(self, user_to_change, field_to_change, updated_field)
                except Exception as e:
                    print(e)
                    return "Failed to update user"
                return "Contact information changed"  # Whatever was written in the acceptance tests
        return "Illegal changed field"

    def edit_user(self, user_to_edit, field_to_change, updated_field, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        if field_to_change == "username" and '*' in updated_field:
            return "Failed to updated user"
        all_field_names = User._meta.get_fields()
        for field in all_field_names:
            if not field.is_relation and field_to_change == field.attname:
                try:
                    DjangoInterface.DjangoInterface.update_user(self, user_to_edit, field_to_change, updated_field)
                except Exception as e:
                    print(e)
                    return "Failed to update user"
                return "User successfully updated"  # Whatever was written in the acceptance tests
        return "Tried to change illegal field"

