from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock, patch

import pandas as pd
from pandas.testing import assert_frame_equal


class TestJsonStrToDF(TestCase):
    def _call_fut(self, *args) -> Any:
        from converter import json_str_to_df

        return json_str_to_df(*args)

    def test_for_s3_image(self) -> None:
        test_json_str = '[{"name": "test", "image_path": ["s3://image.jpg"]}]'

        expected_df = pd.DataFrame({
            'name': ['test'],
            'image_path': [['s3://image.jpg']]
        })
        actual_df = self._call_fut(test_json_str)

        assert_frame_equal(actual_df, expected_df)

    def test_for_https_image(self) -> None:
        test_json_str = '[{"name": "test", "image_path": ["https://image.jpg"]}]'

        expected_df = pd.DataFrame({
            'name': ['test'],
            'image_path': [['https://image.jpg']]
        })
        actual_df = self._call_fut(test_json_str)

        assert_frame_equal(actual_df, expected_df)

    @patch('converter.StringIO')
    def test_return_None_when_without_StringIO(self, StringI0: MagicMock) -> None:
        test_json_str = '[{"name": "test", "image_path": ["https://image.jpg"]}]'

        StringI0.return_value = test_json_str
        actual_df = self._call_fut(test_json_str)

        self.assertEqual(actual_df, None)

    def test_return_None_when_unexpected_char(self) -> None:
        test_json_str = '[{"name": "test"'
        actual_df = self._call_fut(test_json_str)

        self.assertEqual(actual_df, None)
