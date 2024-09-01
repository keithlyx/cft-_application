import unittest
from app import app 

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client() 

    def test_add(self):
        response = self.client.post('/add', data={'num1': '5', 'num2': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 8})

    def test_subtract(self):
        response = self.client.post('/subtract', data={'num1': '10', 'num2': '4'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 6})

    def test_add_with_missing_num2(self):
        response = self.client.post('/add', data={'num1': '5'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 5})

    def test_invalid_input(self):

        response = self.client.post('/add', data={'num1': 'abc', 'num2': 'xyz'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input'})

if __name__ == '__main__':
    unittest.main()
