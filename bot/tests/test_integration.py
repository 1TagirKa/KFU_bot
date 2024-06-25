import unittest
import requests
from unittest.mock import patch


class TestExternalAPIIntegration(unittest.TestCase):
    @patch('requests.post')
    def test_openai_integration(self, mock_post):
        mock_post.return_value.ok = True
        mock_post.return_value.json = lambda: {"choices": [{"text": "test response"}]}

if __name__ == '__main__':
    unittest.main()
