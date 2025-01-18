import os
from enum import Enum
from functools import lru_cache
from pydantic_settings import BaseSettings
from src.app.core.config import settings
from typing import Optional

# Get the current file directory and construct path to .env file
current_file_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_file_dir, "..", "..", ".env")


class DBOption(Enum):
    """Database options enumeration"""
    POSTGRES = "postgres"  # PostgreSQL database
    SQLITE = "sqlite"      # SQLite database


class EnvironmentOption(str, Enum):
    """Environment options enumeration
    
    Defines the different environments the application can run in:
    - LOCAL: Local development environment
    - DEVELOPMENT: Development environment
    - STAGING: Staging/testing environment  
    - PRODUCTION: Production environment
    """
    LOCAL = "local"
    DEVELOPMENT = "development" 
    STAGING = "staging"
    PRODUCTION = "production"


class BaseConfig(BaseSettings):
    """Base configuration class that will be inherited by all environment-specific configs
    
    This class defines all the common configuration settings shared across different
    environments. It uses environment variables with fallback default values.
    
    Settings categories include:
    - Application metadata
    - Environment configuration
    - API settings
    - Documentation settings
    - CORS configuration
    - Logging configuration
    - Rate limiting
    - Security settings
    - LiveKit integration
    """

    # Application metadata settings
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI App")
    APP_DESCRIPTION: str = os.getenv("APP_DESCRIPTION", "FastAPI Application") 
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")

    # Application Server configuration
    PORT: str = os.getenv("PORT", "8000")
    HOST: str = os.getenv("HOST", "localhost")

    # Common settings shared across configurations
    LOG_PATH: str = os.getenv("LOG_PATH", "./logs")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Environment settings
    ENVIRONMENT: EnvironmentOption = os.getenv("ENVIRONMENT", EnvironmentOption.DEVELOPMENT)
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # API configuration
    API_PREFIX: str = os.getenv("API_PREFIX", "api")
    API_VERSION: str = os.getenv("API_VERSION", "v1")

    # Documentation settings
    DOCS_ENABLED: bool = os.getenv("DOCS_ENABLED", "True").lower() == "true"

    # CORS configuration
    CORS_ORIGINS: list[str] = os.getenv("CORS_ORIGINS", "*").split(",")
    CORS_METHODS: list[str] = os.getenv("CORS_METHODS", "*").split(",")
    CORS_HEADERS: list[str] = os.getenv("CORS_HEADERS", "*").split(",")

    # API Documentation URLs
    DOCS_URL: str = os.getenv("DOCS_URL", "/docs")
    REDOC_URL: str = os.getenv("REDOC_URL", "/redoc")
    OPENAPI_URL: str = os.getenv("OPENAPI_URL", "/openapi.json")
    DOCS_ENABLED: bool = os.getenv("DOCS_ENABLED", "True").lower() == "true"

    # Logging configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_PATH: str = os.getenv("LOG_PATH", "./logs")
    LOG_FILENAME: str = os.getenv("LOG_FILENAME", "app.log")
    LOG_ROTATION: str = os.getenv("LOG_ROTATION", "500 MB")
    LOG_RETENTION: str = os.getenv("LOG_RETENTION", "10 days")
    LOG_FORMAT: str = os.getenv("LOG_FORMAT", "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

    # Rate limiting settings
    RATE_LIMIT_ENABLED: bool = os.getenv("RATE_LIMIT_ENABLED", "True").lower() == "true"
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "100"))
    RATE_LIMIT_PERIOD: int = int(os.getenv("RATE_LIMIT_PERIOD", "60"))  # seconds

    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALLOWED_HOSTS: list[str] = os.getenv("ALLOWED_HOSTS", "*").split(",")

    # LiveKit integration settings
    LIVEKIT_API_KEY: str = os.getenv("LIVEKIT_API_KEY", "your-livekit-api-key-here")
    LIVEKIT_API_SECRET: str = os.getenv("LIVEKIT_API_SECRET", "your-livekit-api-secret-here")
    LIVEKIT_HOST: str = os.getenv("LIVEKIT_HOST", "https://api.livekit.com")

    class Config:
        """Pydantic model configuration
        
        Attributes:
            case_sensitive: Maintain case sensitivity for field names
            env_file: Path to the environment file
        """
        case_sensitive = True
        env_file = ".env"
