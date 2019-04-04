class User:

    def __init__(self,username, userpassword, permissions):
        # self.id = userid
        self.username = username
        self.password = userpassword
        self.permissions = permissions
        #permissions [Supervisor, Admin, Instructor, TA]
        # self.pa = userpa
        # self.address = useraddress
        # self.phonenumber = userphonenumber
        # self.email = useremail
