import os
from enum import Enum

from pydantic_settings import BaseSettings
from starlette.config import Config

# current_file_dir = os.path.dirname(os.path.realpath(__file__))
# env_path = os.path.join(current_file_dir, "..", "..", ".env")
# config = {}
# # config = Config(env_path)
#
#
# class AppSettings(BaseSettings):
#     APP_NAME: str = config("APP_NAME", default="FastAPI app")
#     APP_DESCRIPTION: str | None = config("APP_DESCRIPTION", default=None)
#     APP_VERSION: str | None = config("APP_VERSION", default=None)
#     LICENSE_NAME: str | None = config("LICENSE", default=None)
#     CONTACT_NAME: str | None = config("CONTACT_NAME", default=None)
#     CONTACT_EMAIL: str | None = config("CONTACT_EMAIL", default=None)
#
#
# class CryptSettings(BaseSettings):
#     SECRET_KEY: str = config("SECRET_KEY")
#     ALGORITHM: str = config("ALGORITHM", default="HS256")
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
#     REFRESH_TOKEN_EXPIRE_DAYS: int = config("REFRESH_TOKEN_EXPIRE_DAYS", default=7)
#
#
# class DatabaseSettings(BaseSettings):
#     pass
#
#
# class SQLiteSettings(DatabaseSettings):
#     SQLITE_URI: str = config("SQLITE_URI", default="./sql_app.db")
#     SQLITE_SYNC_PREFIX: str = config("SQLITE_SYNC_PREFIX", default="sqlite:///")
#     SQLITE_ASYNC_PREFIX: str = config("SQLITE_ASYNC_PREFIX", default="sqlite+aiosqlite:///")
#
#
# class PostgresSettings(DatabaseSettings):
#     POSTGRES_USER: str = config("POSTGRES_USER", default="postgres")
#     POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD", default="postgres")
#     POSTGRES_SERVER: str = config("POSTGRES_SERVER", default="localhost")
#     POSTGRES_PORT: int = config("POSTGRES_PORT", default=5432)
#     POSTGRES_DB: str = config("POSTGRES_DB", default="postgres")
#     POSTGRES_SYNC_PREFIX: str = config("POSTGRES_SYNC_PREFIX", default="postgresql://")
#     POSTGRES_ASYNC_PREFIX: str = config("POSTGRES_ASYNC_PREFIX", default="postgresql+asyncpg://")
#     POSTGRES_URI: str = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
#     POSTGRES_URL: str | None = config("POSTGRES_URL", default=None)
#
#
# class FirstUserSettings(BaseSettings):
#     ADMIN_NAME: str = config("ADMIN_NAME", default="admin")
#     ADMIN_EMAIL: str = config("ADMIN_EMAIL", default="admin@admin.com")
#     ADMIN_USERNAME: str = config("ADMIN_USERNAME", default="admin")
#     ADMIN_PASSWORD: str = config("ADMIN_PASSWORD", default="!Ch4ng3Th1sP4ssW0rd!")
#
#
# class TestSettings(BaseSettings):
#     TEST_NAME: str = config("TEST_NAME", default="Tester User")
#     TEST_EMAIL: str = config("TEST_EMAIL", default="test@tester.com")
#     TEST_USERNAME: str = config("TEST_USERNAME", default="testeruser")
#     TEST_PASSWORD: str = config("TEST_PASSWORD", default="Str1ng$t")
#
#
# class RedisCacheSettings(BaseSettings):
#     REDIS_CACHE_HOST: str = config("REDIS_CACHE_HOST", default="localhost")
#     REDIS_CACHE_PORT: int = config("REDIS_CACHE_PORT", default=6379)
#     REDIS_CACHE_URL: str = f"redis://{REDIS_CACHE_HOST}:{REDIS_CACHE_PORT}"
#
#
# class ClientSideCacheSettings(BaseSettings):
#     CLIENT_CACHE_MAX_AGE: int = config("CLIENT_CACHE_MAX_AGE", default=60)
#
#
# class RedisQueueSettings(BaseSettings):
#     REDIS_QUEUE_HOST: str = config("REDIS_QUEUE_HOST", default="localhost")
#     REDIS_QUEUE_PORT: int = config("REDIS_QUEUE_PORT", default=6379)
#
#
# class RedisRateLimiterSettings(BaseSettings):
#     REDIS_RATE_LIMIT_HOST: str = config("REDIS_RATE_LIMIT_HOST", default="localhost")
#     REDIS_RATE_LIMIT_PORT: int = config("REDIS_RATE_LIMIT_PORT", default=6379)
#     REDIS_RATE_LIMIT_URL: str = f"redis://{REDIS_RATE_LIMIT_HOST}:{REDIS_RATE_LIMIT_PORT}"
#
#
# class DefaultRateLimitSettings(BaseSettings):
#     DEFAULT_RATE_LIMIT_LIMIT: int = config("DEFAULT_RATE_LIMIT_LIMIT", default=10)
#     DEFAULT_RATE_LIMIT_PERIOD: int = config("DEFAULT_RATE_LIMIT_PERIOD", default=3600)
#
# # Environment Options
# class EnvironmentOption(str, Enum):
#     LOCAL = "local"
#     DEVELOPMENT = "development"
#     STAGING = "staging"
#     PRODUCTION = "production"
#
#
class DBOption(Enum):
    POSTGRES = "postgres"
    SQLITE = "sqlite"

#
# class EnvironmentSettings(BaseSettings):
#     # Settings class
#     ENVIRONMENT: EnvironmentOption = config(key="ENVIRONMENT", default=EnvironmentOption.LOCAL)
#     APP_NAME: str = "FastAPI App"
#     APP_DESCRIPTION: str = "FastAPI Application"
#     APP_VERSION: str = "1.0.0"
#     DB_ENGINE: DBOption = config("DB_ENGINE", default="sqlite")
#
#     class Config:
#         env_file = ".env"
#         use_enum_values = True
#
#
#
# db_type = PostgresSettings
# if config("DB_ENGINE", default="sqlite") == "sqlite":
#     db_type = SQLiteSettings
#
#
# class Settings(
#     AppSettings,
#     db_type,
#     CryptSettings,
#     FirstUserSettings,
#     TestSettings,
#     RedisCacheSettings,
#     ClientSideCacheSettings,
#     RedisQueueSettings,
#     RedisRateLimiterSettings,
#     DefaultRateLimitSettings,
#     EnvironmentSettings,
# ):
#     pass
#
#
# settings = Settings()
settings = {'DB_ENGINE': 'None'}
