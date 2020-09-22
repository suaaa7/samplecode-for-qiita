from dataclasses import dataclass


@dataclass(frozen=True)
class BaseConfig:
    version: str
    model_path: str
    model_s3_bucket: str
    model_file_name: str

    def generate_model_path(self) -> str:
        return "{}/{}/{}".format(
            self.model_path,
            self.version,
            self.model_file_name
        )

    def generate_model_s3_path(self) -> str:
        return "s3://{}/{}/{}".format(
            self.model_s3_bucket,
            self.version,
            self.model_file_name
        )


@dataclass(frozen=True)
class Train:
    batch_size: int = 16
    epoch: int = 10


@dataclass(frozen=True)
class Test:
    batch_size: int = 16


@dataclass(frozen=True)
class Config(BaseConfig):
    version: str = "v1.0.0"
    model_path: str = "/ops/models"
    model_s3_bucket: str = "models"
    model_file_name: str = "model.pth"
    train: Train = Train()
    test: Test = Test()
