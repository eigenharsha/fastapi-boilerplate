from src.app.setup import create_application
from src.config.settings import get_settings
from src.core.logger import logger

settings = get_settings()

# Create the FastAPI application using our setup utility
app = create_application()


@app.on_event("startup")
async def startup_event():
    """
    Initialize application on startup.
    Runs when the application starts.
    """
    logger.info(f"Starting {settings.APP_NAME} in {settings.ENVIRONMENT} mode")
    logger.info(f"API documentation available at: /docs")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Cleanup on shutdown.
    Runs when the application is shutting down.
    """
    logger.info(f"Shutting down {settings.APP_NAME}")
