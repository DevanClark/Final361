class Login:

    def __init__(self, django_interface):
        self.django_interface = django_interface

    def login_to_database(self, username, password):
        try:
            user = self.django_interface.login_username(username)
        except Exception as e:
            return None
        return user

    def logout(self):
        return None

