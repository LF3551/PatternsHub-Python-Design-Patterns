import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from UserService.user_service import app

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_user(self):
        response = self.app.post('/user/create', json={'id': '001', 'name': 'John Doe'})
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        self.app.post('/user/create', json={'id': '001', 'name': 'John Doe'})
        response = self.app.get('/user/001')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', str(response.data))

if __name__ == '__main__':
    unittest.main()
