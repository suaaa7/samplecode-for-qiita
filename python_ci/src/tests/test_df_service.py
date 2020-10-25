from unittest import TestCase, main, skip
from unittest.mock import patch

import pandas as pd
from pandas.api.types import is_integer_dtype
from pandas.testing import assert_frame_equal

from src.df_service import DFService


class TestDFService(TestCase):
    def setUp(self) -> None:
        self.patcher = patch('src.df_service.ImageDownloadService.get_local_path')
        self.m_get_local_path = self.patcher.start()

        self.service = DFService()
        self.test_df = pd.DataFrame({
            'num': [1, 2],
            'image_hash': [
                ['aaaaa'],
                ['aaaaa', 'aaaaa']
            ],
            'image_path': [
                ['s3://test_image.jpg'],
                ['s3://test_image.jpg', 's3://test_image.jpg']
            ]
        })
        self.test_base_dir = '/home/test-user'

    def tearDown(self) -> None:
        self.patcher.stop()

    def test_return_empty_df(self) -> None:
        self.m_get_local_path.return_value = None

        actual_df = self.service.swap_and_remove_path(
            self.test_df,
            self.test_base_dir
        )

        self.assertTrue(actual_df.empty)
        self.assertEqual(self.m_get_local_path.call_count, 3)
        self.m_get_local_path.assert_called_with(
            image_hash='aaaaa',
            base_dir=self.test_base_dir
        )

    def test_return_empty_df_when_base_dir_is_none(self) -> None:
        self.m_get_local_path.return_value = None

        actual_df = self.service.swap_and_remove_path(self.test_df)

        self.assertTrue(actual_df.empty)
        self.assertEqual(self.m_get_local_path.call_count, 3)
        self.m_get_local_path.assert_called_with(
            image_hash='aaaaa',
            base_dir=None
        )

    def test_return_expected_df(self) -> None:
        self.m_get_local_path.return_value = '/opt/program/test_image.jpg'

        expected_df = pd.DataFrame({
            'num': [1, 2],
            'image_hash': [
                ['aaaaa'],
                ['aaaaa', 'aaaaa']
            ],
            'image_path': [
                ['/opt/program/test_image.jpg'],
                ['/opt/program/test_image.jpg', '/opt/program/test_image.jpg']
            ]
        })
        actual_df = self.service.swap_and_remove_path(self.test_df)

        self.assertTrue(is_integer_dtype(actual_df['num']))
        assert_frame_equal(actual_df, expected_df)
        self.assertEqual(self.m_get_local_path.call_count, 3)

    def test_return_expected_df_when_get_local_path_return_none(self) -> None:
        self.m_get_local_path.side_effect = [
            '/opt/program/test_image.jpg',
            None,
            '/opt/program/test_image.jpg'
        ]

        expected_df = pd.DataFrame({
            'num': [1],
            'image_hash': [
                ['aaaaa']
            ],
            'image_path': [
                ['/opt/program/test_image.jpg']
            ]
        })
        actual_df = self.service.swap_and_remove_path(self.test_df)

        self.assertTrue(is_integer_dtype(actual_df['num']))
        assert_frame_equal(actual_df, expected_df)
        self.assertEqual(self.m_get_local_path.call_count, 3)

    @skip('Use unittest.skip')
    def test_tmp(self) -> None:
        pass


if __name__ == '__main__':
    main()
