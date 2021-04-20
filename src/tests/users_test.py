import unittest
from users import Userlist, Users
from characters import Character

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.user = Users("testname")
        self.char = Character("testchar")

    def test_constructor_name_correct(self):
        self.assertEqual(self.user.name, "testname")

    def test_constructor_dict_correct(self):
        self.assertDictEqual(self.user.characterlist, {})
    
    def test_add_character(self):
        self.user.add_character(self.char)
        self.assertEqual(self.user.characterlist["testchar"].name, "testchar")

    def test_give_characterlist(self):
        self.assertDictEqual(self.user.give_characterlist(), {})

class TestUserlist(unittest.TestCase):
    def setUp(self):
        pass
