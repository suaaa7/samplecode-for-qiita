import json
from unittest import TestCase, main

from flask_app.app import app

print('In app_test')

class AppTestCase(TestCase):
    def setUp(self):
        print('Call setUp in AppTestCase')
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        response = self.client.get('/')
        self.assertEqual(response.content_type, 'application/json')

    def test_predict(self):
        response = self.client.post('/predict')
        self.assertEqual(response.status_code, 200)

    def test_predict_content(self):
        response = self.client.post('/predict')
        self.assertEqual(response.content_type, 'application/json')

    def test_predict_data(self):
        response = self.client.post('/predict')
        self.assertIsInstance(json.loads(response.data)['result'], float)

if __name__ == '__main__':
    main()
