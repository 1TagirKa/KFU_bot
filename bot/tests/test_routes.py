import unittest
from flask import Flask
from api.routes import setup_routes

class TestAPIRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        setup_routes(self.app)
        self.client = self.app.test_client()

    def test_analyze_satisfaction(self):
        response = self.client.post('/analyze_satisfaction', json={'scores': [1, 2, 3, 4, 5]})
        self.assertEqual(response.status_code, 200)
        self.assertIn('satisfaction_level', response.get_json())

if __name__ == '__main__':
    unittest.main()