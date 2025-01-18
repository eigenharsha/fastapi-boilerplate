from loguru import logger
from src.config.settings import get_settings
from src.core.logging import setup_logging

# Initialize logging
setup_logging(get_settings())

# Create a middleware to log API requests
from fastapi import Request


async def log_request(request: Request, response=None):
    """Log API request details."""
    logger.bind(access=True).info(
        f"{request.method} {request.url.path} - "
        f"Status: {getattr(response, 'status_code', 'N/A')} - "
        f"Client: {request.client.host if request.client else 'Unknown'}"
    )

# Export configured logger
__all__ = ["logger", "log_request"]