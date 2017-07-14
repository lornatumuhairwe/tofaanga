import unittest
import context
from app.bucketlistmodel import User

class BucketlistModelTest(unittest.TestCase):
    def setUp(self):
        """Initialisation before each test """
        self.user = User('lornatumuhairwe@gmail.com')
        self.bucketlists = {'lornatumuhairwe@gmail.com': {'Cities': {}}}

    def test_user_Instance(self): #this test ensures that the object is always properly initialized
        self.assertIsInstance(self.user, User, msg='object missing parameters')

    def test_bucketlist_is_added_to_bucketlists_dictionary(self): # test ensures that bucketlist is added
        self.assertEqual({'lornatumuhairwe@gmail.com': {'Cities': {}, 'Premier League': {}}},
                         self.user.create_user_bucketlist('Premier League'))

    def test_return_false_if_bucketlist_to_be_added_exists(self):
        self.assertEqual(False, self.user.create_user_bucketlist('Cities'))

    def test_empty_users_should_not_be_added_to_user_dictionary(self):
        self.assertEqual(self.user.create_user_bucketlist(''), False)

    def test_delete_bucketlist(self):
        self.assertEqual({'lornatumuhairwe@gmail.com': {}}, self.user.delete_bucketlist('Cities'))

    def test_add_item_to_existing_bucketlist(self):
        self.assertEqual({'lornatumuhairwe@gmail.com': {'Cities': {'Nairobi': ['Incoomplete', '2017-07-15']}}},
                         self.user.add_item_to_bucketlist('Cities', 'Nairobi', ['Incoomplete', '2017-07-13']))

if __name__=='__main__':
    unittest.main()