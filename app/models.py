users = {'xr': ['X', '1920', 'asd']} # dictionary stores all users who register.
logged_in = [None] # list that holds the current_user, contains None if no current user

class BucketListApp(object):
    """Intializes an object of BuckListApp. email and password are only compulsory arguments"""
    def __init__(self, email, password, name=None, dob=None, cpassword=None):
        self.name = name
        self.email = email
        self.dob = dob
        self.password = password # password, password must equal to confirm password inorder to save
        self.cpassword = cpassword  # confirm password, allows a user to enter password twice during signup in order to save

    def signup(self):
        """Implements signup feature"""
        if self.email and self.password:
            if self.email in users: # flag 'user exists' if the sign up details match the ones of an existing user in user dictionary
                return 'User already exists'
            else:
                if self.password == self.cpassword: # password, password must equal to confirm password inorder to save
                    users[self.email] = [self.name, self.dob, self.password]
                    return users
                else:
                    return 'password mismatch'
        else:
            return 'No user name given'

    def login(self):
        """Implements login feature"""
        if self.email in users:
            if self.password == users[self.email][2]: # if the password entered by the user is similar to the password in user dictionary
                logged_in[0] = self.email # logs in user by putting email in first position of logged_in list
                return 'Logged in'
            else:
                return 'Incorrect password'
        else:
            return 'Unknown user'

    def logout(self, emaill):
        """Implements logout feature"""
        if emaill in logged_in:
            logged_in.remove(emaill) # logs out user by removing email from logged_in list
            return 'Logged out'
        else:
            return 'User is not logged in'
