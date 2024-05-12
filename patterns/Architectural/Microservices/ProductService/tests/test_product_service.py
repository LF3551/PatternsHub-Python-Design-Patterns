import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from ProductService.product_service import app

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_product(self):
        response = self.app.post('/product/create', json={'id': '101', 'name': 'Apple'})
        self.assertEqual(response.status_code, 201)

    def test_get_product(self):
        self.app.post('/product/create', json={'id': '101', 'name': 'Apple'})
        response = self.app.get('/product/101')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Apple', str(response.data))

if __name__ == '__main__':
    unittest.main()
