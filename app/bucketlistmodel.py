from app import models
bucketlists = {} # dictionary stores all the bucketlists and items for the signed users.
current_user_bucketlists = [] # list that holds the current users bucketlists

class User(object):
    """Initializes user object with the email argument"""
    def __init__(self, email): # email belongs to the logged in user
        self.email = email

    def create_user_bucketlist(self, name):
        """Implements create user bucketlist feature"""
        if name and name not in bucketlists:
                if self.email in bucketlists:
                    bucketlists[self.email][name] = {} # creates empty dictionary in bucketlists with bucketlist name as key
                else:
                    bucketlists[self.email] = {} # creates empty dictionary in bucketlists dictionary with current user as key
                    bucketlists[self.email][name] = {} # creates empty dictionary in current user dictionary with bucketlist name as key
                return bucketlists
        else:
            return False

    def view_user_bucketlist(self, email):
        """Implements view user bucketlists feature"""
        user_bucketlists = []
        if email in bucketlists:
            for bucketlist in bucketlists[email]:
                user_bucketlists.append(bucketlist)
            global current_user_bucketlists # to ensure that current_user_bucketlists can be manipulated in the scope
            current_user_bucketlists = user_bucketlists
            return user_bucketlists
        else:
            bucketlists[email] = {}
            current_user_bucketlists = user_bucketlists
            global current_user_bucketlists
            current_user_bucketlists = user_bucketlists
            return user_bucketlists

    def delete_bucketlist(self, name):
        """Implements delete feature"""
        if name: # makes sure the name fielf is not empty and
            del bucketlists[models.logged_in[0]][name]
            return bucketlists

    def add_item_to_bucketlist(self, bucketlist, title, details):
        """Implements add item to bucketlist feature"""
        bucketlists[models.logged_in[0]][bucketlist][title] = details # creates dictionary with title of activity as key
        return bucketlists                                             # and details of activity as values


    def view_items_in_bucketlist(self, bucketlist):
        """Implements view items in bucketlist feature"""
        all_items = []
        if bucketlists[models.logged_in[0]][bucketlist]: # returns bucketlists of current user
            for items, values in bucketlists[models.logged_in[0]][bucketlist].items():# iterates through items in bucketlists of current user
                #return items, values
                activity = (items, values)
                all_items.append(activity) # to return all items in current users bucketlists
            return all_items
        else:
            return None