from app import models
bucketlists = {}
current_user_bucketlists = []

class User(object):

    def __init__(self, email):#email belongs to the logged in user
        self.email = email
        # self.bucketlist = []

    def create_user_bucketlist(self, name):
        if name and name not in bucketlists:
                if self.email in bucketlists:
                    bucketlists[self.email][name] = {}
                else:
                    bucketlists[self.email] = {}
                    bucketlists[self.email][name] = {}
                return bucketlists
        else:
            return False

    def view_user_bucketlist(self, email):
        user_bucketlists = []
        if email in bucketlists:
            for bucketlist in bucketlists[email]:
                user_bucketlists.append(bucketlist)
            global current_user_bucketlists
            current_user_bucketlists = user_bucketlists
            return user_bucketlists
        else:
            bucketlists[email] = {}
            current_user_bucketlists = user_bucketlists
            global current_user_bucketlists
            current_user_bucketlists = user_bucketlists
            return user_bucketlists

    def update_bucketlist(self, name):
        pass

    def delete_bucketlist(self, name):
        if name and name not in bucketlists:
            del bucketlists[models.logged_in[0]][name]
            return bucketlists

    def add_item_to_bucketlist(self, bucketlist, title, details):
        bucketlists[models.logged_in[0]][bucketlist][title] = details
        return bucketlists

    def view_items_in_bucketlist(self, bucketlist):
        # for key, value in bucketlists[models.logged_in][bucketlist].items():
        print("-----------------")
        print (bucketlists[models.logged_in[0]][bucketlist])

        if bucketlists[models.logged_in[0]][bucketlist]:
            for items, values in bucketlists[models.logged_in[0]][bucketlist].items():
                print ('-------list items are---')
                print (items, values)
                return items, values
        else:
            return None

if __name__ == "__main__":
    name1 = input('Name: ')
    bucketlist = input('Add bucketlist to account: ')
    appp = User(name1)
    print (appp.create_bucketlist(bucketlist))
    print (appp.add_item_to_bucketlist('mk', ['Drive to Kampala', 1995, 'Not Done']))
    #print (appp.view_bucketlist(ownerr))