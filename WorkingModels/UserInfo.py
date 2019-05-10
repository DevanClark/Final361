class UserInfo:
    def __init__(self, user_name, password, permissions, address, email, phone_number):
        self.user_name = user_name
        self.password = password
        self.address = address
        self.email = email
        self.phone_number = phone_number
        if permissions[0] == "1":
            self.permissions = "supervisor"
        elif permissions[1] == "1":
            self.permissions = "admin"
        elif permissions[2] == "1":
            self.permissions = "instructor"
        else:
            self.permissions = "ta"
