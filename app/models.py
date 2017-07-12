users = {'xr': ['X', '1920', 'asd']}
logged_in = []

class BucketListApp(object):
    def __init__(self, email, password, name=None, dob=None, cpassword=None):
        self.name = name
        self.email = email
        self.dob = dob
        self.password = password
        self.cpassword = cpassword
        #self.users = {}
        #self.users = {'xr': ['X', '1992', 'asd']}
        #self.logged_in = []

    def signup(self):
        if self.email and self.password:
            if self.email in users:
                return 'User already exists'
            else:
                if self.password == self.cpassword:
                    users[self.email] = [self.name, self.dob, self.password]
                    return users
                else:
                    return 'password mismatch'
        else:
            return 'No user name given'

    def login(self):
        if self.email in users:
            if self.password == users[self.email][2]:
                logged_in.append(self.email)
                #print (logged_in)
                return 'Logged in'
            else:
                return 'Incorrect password'
        else:
            return 'Unknown user'

    def logout(self, emaill):
        if emaill in logged_in:
            logged_in.remove(emaill)
            return 'Logged out'
        else:
            return 'User is not logged in'

if __name__ == "__main__":
    name1 = input('Name: ')
    email1 = input('Email: ')
    dob1 = input('DOB: ')
    password1 = input('Password: ')
    cpassword1 = input('cPassword: ')
    appp = BucketListApp(email1, password1, name1, dob1, cpassword1)
    print (appp.signup())
    print ('You can now login!\n')
    email1 = input('Email: ')
    password1 = input('Password: ')
    print (appp.login())