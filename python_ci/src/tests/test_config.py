from dataclasses import FrozenInstanceError
from unittest import TestCase, main

from src.config import BaseConfig, Config


class TestConfig(TestCase):
    def test_generate_path(self):
        config = BaseConfig(
            version="v0.0.0",
            model_path="/opt/models",
            model_s3_bucket="models",
            model_file_name="model.pth"
        )

        expected_model_path = "/opt/models/v0.0.0/model.pth"
        expected_model_s3_path = "s3://models/v0.0.0/model.pth"

        self.assertEqual(config.generate_model_path(), expected_model_path)
        self.assertEqual(config.generate_model_s3_path(), expected_model_s3_path)

    def test_config_can_call_method(self):
        config = Config()
        config.generate_model_path()
        config.generate_model_s3_path()

    def test_config_is_immutable(self):
        config = Config()

        with self.assertRaises(FrozenInstanceError):
            config.version = "v0.0.0"

        with self.assertRaises(FrozenInstanceError):
            config.train.epoch = 10000

        with self.assertRaises(FrozenInstanceError):
            config.test.batch_siz = 64


if __name__ == '__main__':
    main()
