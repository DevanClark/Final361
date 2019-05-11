from Final.DjangoInterface import DjangoInterface
from Final.models import *

django_interface = DjangoInterface()


# A class designed to handle the creating, editing, and deleting of users
class UserEdits:

    # Add A User
    # Username to be assigned to the user
    # Password to be assigned to the user
    # Permissions to be assigned to the user
    # Address to be assigned to the user
    # Phone number to be assigned to the user
    # Email to be assigned to the user
    # logged_in_user is the user attempting to add a user
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
            django_interface.create_user(username, password, permissions, address, phonenumber, email)
        except Exception as e:
            print(e)
            return "Failed to add user."
        return "User successfully added"

    # Delete a user
    # usertodelete is the username of the user to be deleted
    # logged_in_user is the user attempting to delete a user
    def delete_user(self, usertodelete, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            return "Illegal permissions to do this action"
        if usertodelete == logged_in_user.username:
            return "Unable to delete active user"
        try:
            django_interface.delete_user(usertodelete)
        except Exception as e:
            return "User unsuccessfully deleted"
        return "User successfully deleted"

    # Change_contact
    # This method is specifically for a user to edit his/her own contact/personal information
    # User to change is the username of the user who is changing his/her information
    # Field to change is the field the user wants to change (address, phone number, email etc.)
    # Updated Field is the new value meant to be assigned to that field (home address is now Illinois)
    def change_contact(self, user_to_change, field_to_change, updated_field):
        if field_to_change == "username":
            return "Invalid parameter for this command"
        all_field_names = User._meta.get_fields()
        for field in all_field_names:
            if not field.is_relation and field_to_change == field.attname:
                try:
                    django_interface.update_user(user_to_change, field_to_change, updated_field)
                except Exception as e:
                    print(e)
                    return "Failed to update user"
                return "Contact information changed"
        return "Illegal changed field"

    # Edit User
    # This method is the method meant to edit any user's info, permissions, etc.
    # Field_to_change is the field that will be updated(phone number, permissions, etc.)
    # Updated_field is the new value to be assigned to the field
    # Logged_in_user is the user attempting to edit users
    def edit_user(self, user_to_edit, field_to_change, updated_field, logged_in_user):
        if logged_in_user.permissions[0] != '1' and logged_in_user.permissions[1] != '1':
            print("Illegal permissions to do this action")
            return "Illegal permissions to do this action"
        if field_to_change == "username" and '*' in updated_field:
            print("Failed to updated user")
            return "Failed to updated user"
        all_field_names = User._meta.get_fields()
        for field in all_field_names:
            if not field.is_relation and field_to_change == field.attname:

                try:
                    django_interface.update_user(user_to_edit, field_to_change, updated_field)
                except Exception as e:
                    print(e)
                    return "Failed to update user"
                return "User successfully updated"  # Whatever was written in the acceptance tests
        return "Tried to change illegal field"
