import os
from loguru import logger


class BaseConfig:
    ENV = "base"
    PROJECT_NAME = "qd_transformers"
    API_PREFIX = "/api"
    PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


class TestConfig(BaseConfig):
    ENV = "test"


class DevConfig(BaseConfig):
    ENV = "dev"


class StageConfig(BaseConfig):
    ENV = "stage"


class ProdConfig(BaseConfig):
    ENV = "prod"


configs = BaseConfig()
if os.getenv("ENV") == "dev":
    configs = DevConfig()
elif os.getenv("ENV") == "test":
    configs = TestConfig()
elif os.getenv("ENV") == "stage":
    configs = StageConfig()
elif os.getenv("ENV") == "prod":
    configs = ProdConfig()
else:
    logger.warning(f"No environment set, using default configs. ENV: {configs.ENV}")
    configs = BaseConfig()


print(f"Using configs: {configs.ENV}")
