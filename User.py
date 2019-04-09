class User:

    def __init__(self, userid, username, userpassword, permissions, useraddress, userphonenumber, useremail):
        self.id = userid
        self.username = username
        self.password = userpassword
        self.permissions = permissions
        self.address = useraddress
        self.phonenumber = userphonenumber
        self.email = useremail
