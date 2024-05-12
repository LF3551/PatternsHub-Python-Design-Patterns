import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Layered.layered import UserDataAccess, UserManager, UserAPI

class TestLayeredArchitecture(unittest.TestCase):
    def setUp(self):
        self.data_access = UserDataAccess()
        self.user_manager = UserManager(self.data_access)
        self.user_api = UserAPI(self.user_manager)

    def test_user_creation(self):
        result = self.user_api.register_user("001", {"name": "Alice", "email": "alice@example.com"})
        self.assertEqual(result, "User created")
        self.assertIn("001", self.data_access.users)

    def test_duplicate_user_creation(self):
        self.user_api.register_user("001", {"name": "Alice", "email": "alice@example.com"})
        result = self.user_api.register_user("001", {"name": "Alice", "email": "alice@example.com"})
        self.assertEqual(result, "User already exists")

    def test_get_user_info(self):
        self.user_api.register_user("001", {"name": "Alice", "email": "alice@example.com"})
        user = self.user_api.get_user_info("001")
        self.assertEqual(user, {"name": "Alice", "email": "alice@example.com"})

    def test_get_nonexistent_user(self):
        result = self.user_api.get_user_info("002")
        self.assertEqual(result, "User not found")

if __name__ == '__main__':
    unittest.main()
