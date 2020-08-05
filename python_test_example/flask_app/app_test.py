import json
from unittest import TestCase, main
from unittest.mock import MagicMock, patch

print('In app_test')

class AppTestCase(TestCase):
    def setUp(self):
        print('Call setUp in AppTestCase')

        self.load_model_patcher = patch('flask_app.model.load_model')
        self.load_model_m = self.load_model_patcher.start()
        self.load_model_m.return_value = 'test'

        from flask_app.app import app
        self.client = app.test_client()

    def tearDown(self):
        self.load_model_patcher.stop()

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

    @patch('flask_app.service.Service.check_model', return_value=False)
    def test_predict_503(self, mock: MagicMock):
        response = self.client.post('/predict')
        self.assertEqual(response.status_code, 503)

if __name__ == '__main__':
    main()
