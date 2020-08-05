from unittest import TestCase, main
from unittest.mock import MagicMock, call, patch

from mock.my_class import MyClass

class MyClassTestCase(TestCase):
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if args[0] == 'http://example.com/test.json':
            return MockResponse({'key1': 'value1'}, 200)
        elif args[0] == 'http://example.com/another_test.json':
            return MockResponse({'key2': 'value2'}, 200)

        return MockResponse(None, 404)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch_json(self, mock_get: MagicMock):
        my_class = MyClass()

        json_data = my_class.fetch_json('http://example.com/test.json')
        self.assertEqual(json_data, {'key1': 'value1'})
        json_data = my_class.fetch_json('http://example.com/another_test.json')
        self.assertEqual(json_data, {'key2': 'value2'})
        json_data = my_class.fetch_json('http://no_example.com/test.json')
        self.assertIsNone(json_data)

        self.assertIn(
            call('http://example.com/test.json'), mock_get.call_args_list
        )
        self.assertIn(
            call('http://example.com/another_test.json'), mock_get.call_args_list
        )

        self.assertEqual(len(mock_get.call_args_list), 3)

if __name__ == '__main__':
    main()
