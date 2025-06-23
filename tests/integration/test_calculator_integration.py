from unittest import TestCase

import requests

BASE_URL = "http://localhost:5000"

class Test(TestCase):
    def test_plus(self):
        data = {"num1": 5, "num2": 3}
        response = requests.post(f"{BASE_URL}/plus", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{"result": 8})

    def test_minus(self):
        data = {"num1": 10, "num2": 4}
        response = requests.post(f"{BASE_URL}/minus", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{"result": 6})

    def test_multiply(self):
        data = {"num1": 7, "num2": 2}
        response = requests.post(f"{BASE_URL}/multiply", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 14})

    def test_divide(self):
        data = {"num1": 15, "num2": 3}
        response = requests.post(f"{BASE_URL}/divide", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{"result": 5})