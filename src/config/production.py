# config/production.py
from src.config.base import BaseConfig, EnvironmentOption


class ProductionConfig(BaseConfig):
    """Production-specific configuration"""
    ENVIRONMENT: EnvironmentOption = EnvironmentOption.PRODUCTION
    DEBUG: bool = False
    DOCS_ENABLED: bool = False  # Disable docs in production

    class Config:
        env_file = ".env.production"
