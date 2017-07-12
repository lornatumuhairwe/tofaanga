bucketlists = {}

class User(object):

    def __init__(self, email):#email belongs to the logged in user
        self.email = email

    def create_user_bucketlist(self, name):
        if self.email in bucketlists:
            bucketlists[self.email][name] = {}
        else:
            bucketlists[self.email] = {}
            bucketlists[self.email][name] = {}
        return bucketlists

    def view_user_bucketlist(self, email):
        user_bucketlists = []
        if email in bucketlists:
            for bucketlist in bucketlists[email]:
                user_bucketlists.append(bucketlist)
            return user_bucketlists
        else:
            bucketlists[email] = {}
            return user_bucketlists

    def update_bucketlist(self, name):
        pass

    def delete_bucketlist(self):
        pass

    def add_item_to_bucketlist(self, bucketlist, item):
        if bucketlist in self.bucketlists:
            self.bucketlists[bucketlist].append(item)
            return self.bucketlists
        else:
            self.bucketlists[bucketlist] = []
            self.bucketlists[bucketlist].append(item)
            return self.bucketlists

if __name__ == "__main__":
    name1 = input('Name: ')
    bucketlist = input('Add bucketlist to account: ')
    appp = User(name1)
    print (appp.create_bucketlist(bucketlist))
    print (appp.add_item_to_bucketlist('mk', ['Drive to Kampala', 1995, 'Not Done']))
    #print (appp.view_bucketlist(ownerr))