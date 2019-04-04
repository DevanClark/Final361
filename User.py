class User:

    username = "blankUser"
    password = "blankPass"
    permissions = [0, 0, 0, 0]

    def __init__(self, username, password, permissions):
        # self.id = userid
        self.username = username
        self.password = password
        self.permissions = permissions
        #permissions [Supervisor, Admin, Instructor, TA]
        # self.pa = userpa
        # self.address = useraddress
        # self.phonenumber = userphonenumber
        # self.email = useremail
