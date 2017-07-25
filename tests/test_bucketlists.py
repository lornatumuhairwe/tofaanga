import unittest
import context
from app.bucketlistmodel import User, bucketlists, models

class BucketlistModelTest(unittest.TestCase):
    def setUp(self):
        """Initialisation before each test """
        self.user = User('lornatumuhairwe@gmail.com')
        self.bucketlists = bucketlists

    def test_user_Instance(self): #this test ensures that the object is always properly initialized
        self.assertIsInstance(self.user, User, msg='object missing parameters')

    def test_bucketlist_is_added_to_bucketlists_dictionary_and_can_be_deleted(self): # test ensures that bucketlist is added
        models.logged_in = ['lornatumuhairwe@gmail.com']
        self.assertEqual({'lornatumuhairwe@gmail.com': {'Cities': {}, 'Premier League': {'ManU': ['13/11/1994', 'incomplete']}}},
                         self.user.create_user_bucketlist('Cities'))
        self.assertEqual(
            {'lornatumuhairwe@gmail.com': {'Premier League': {'ManU': ['13/11/1994', 'incomplete']}}},
            self.user.delete_bucketlist('Cities'))

    def test_return_false_if_bucketlist_to_be_added_is_empty(self):
        self.assertEqual(False, self.user.create_user_bucketlist(''))
    #
    def test_return_false_if_bucketlist_to_be_added_exists(self):
        self.assertEqual(False, self.user.create_user_bucketlist('Premier League'))

    def test_delete_non_existent_bucketlist(self):
        models.logged_in = ['lornatumuhairwe@gmail.com']
        self.assertEqual('Cannot delete a buckelist with no name', self.user.delete_bucketlist(''))


if __name__=='__main__':
    unittest.main()