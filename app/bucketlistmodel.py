bucketlists = {'ltumuhairwe@outlook.com': {'Travel to Kampala': ['Sit on Naguru Hill', 'Visit the Kasubi tombs'],
                                           'Travel to Mbarara': ['Long horns', 'Visit the River']}}

class BucketList(object):

    def __init__(self, owner, name, items=None):
        self.name = name
        self.owner = owner
        self.items = items
        #self.bucketlists = {}

    def create_bucketlist(self):
        bucketlists[self.owner] = {}#first create the owners keys in the bucketlist dict
        bucketlists[self.owner][self.name] =  []#create bucketlist as an inner dictionary
        return bucketlists

    def view_bucketlist(self, owner):
        if owner in bucketlists:
            for bucketlist, items in bucketlists[owner].items():
                return (bucketlist, items)

    def update_bucketlist(self, name):
        pass

    def delete_bucketlist(self):
        pass

if __name__ == "__main__":
    # name1 = input('Name: ')
    ownerr = input('Owner: ')
    # dob1 = input('DOB: ')
    name = input('Bucklist name: ')
    # cpassword1 = input('cPassword: ')
    appp = BucketList(ownerr, name)
    print (appp.create_bucketlist())
    print (appp.view_bucketlist(ownerr))