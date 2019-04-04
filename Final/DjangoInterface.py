from Final.models import *

class DjangoInterface():

    def login_username(self, username):
        user = User.objects.get(username = username)
        if user is None:
            return ""
        return user


