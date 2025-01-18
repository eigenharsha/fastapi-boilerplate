# config/development.py
from functools import lru_cache

from src.config.base import BaseConfig, EnvironmentOption

from src.config.dev import DevelopmentConfig
from src.config.production import ProductionConfig

@lru_cache()
def get_settings(environment: str | None = None) -> BaseConfig:
    """
    Factory function to get the appropriate settings based on environment.
    Uses environment variable or passed parameter to determine which config to use.

    The @lru_cache decorator ensures we only create one instance of the settings.
    """

    try:
        settings = BaseConfig()
        environment = settings.ENVIRONMENT
    except Exception:
        environment = EnvironmentOption.DEVELOPMENT

    configs = {
        EnvironmentOption.DEVELOPMENT: DevelopmentConfig,
        EnvironmentOption.PRODUCTION: ProductionConfig
    }

    config_class = configs.get(environment, DevelopmentConfig)
    return config_class()
