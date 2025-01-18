# config/development.py
from src.config.base import BaseConfig, EnvironmentOption


class DevelopmentConfig(BaseConfig):
    """Development-specific configuration"""
    ENVIRONMENT: EnvironmentOption = EnvironmentOption.DEVELOPMENT
    DEBUG: bool = True

    # Override any other settings specific to development
    class Config:
        env_file = ".env.development"
