#!/usr/bin/env python3
"""
Nova Platform Startup Script
---------------------------

This script initializes and runs the Nova platform with proper configuration
and documentation support. It handles:

1. Environment setup
2. Application configuration
3. FastAPI server initialization with OpenAPI/ReDoc documentation
4. Logging configuration
5. Database connections
6. Agent initialization

Usage:
    python run.py [--port PORT] [--host HOST] [--reload] [--workers WORKERS]

Example:
    python run.py --port 8000 --host 0.0.0.0 --workers 4
"""
from sys import api_version

import uvicorn
import click
import sys
import os
from pathlib import Path
from typing import Optional

from loguru import logger

from src.app.main import app
from src.config.base import EnvironmentOption
from src.config.settings import get_settings
from src.core.logging import setup_logging

settings = get_settings()

# Add src directory to Python path
src_path = str(Path(__file__).parent)
if src_path not in sys.path:
    sys.path.insert(0, src_path)


def configure_app_settings(environment: Optional[str] = None) -> None:
    """
    Configure application settings based on environment.

    Args:
        environment: The environment to run the application in (dev/test/prod)
    """
    if environment:
        os.environ["ENVIRONMENT"] = environment
    else:
        os.environ["ENVIRONMENT"] = EnvironmentOption.DEVELOPMENT

    # Ensure required directories exist
    for directory in ["logs", "data/stock_tweets"]:
        Path(directory).mkdir(parents=True, exist_ok=True)


def print_startup_banner(host: str, port: int) -> None:
    """Print a fancy startup banner with configuration info."""
    banner = f"""
    ╔══════════════════════════════════════════════════════╗
    ║             ANGULA BOILERPLATE(FASTAPI)              ║
    ╚══════════════════════════════════════════════════════╝

    Version: {settings.APP_VERSION}
    Environment: {settings.ENVIRONMENT}
    Root: http://{host}:{port}
    API Docs: http://{host}:{port}/docs
    ReDoc: http://{host}:{port}/redoc
    Health Check: http://{host}:{port}/{settings.API_PREFIX}/{settings.API_VERSION}/health

    Logger Level: {settings.LOG_LEVEL}
    Log Path: {Path('../logs').absolute()}
    Data Path: {Path('data').absolute()}
    """
    print(banner)


@click.command()
@click.option('--port', default=8000, help='Port to run the server on')
@click.option('--host', default="127.0.0.1", help='Host to run the server on')
@click.option('--reload', is_flag=True, help='Enable auto-reload on code changes')
@click.option('--workers', default=1, help='Number of worker processes')
@click.option('--env', default="dev", help='Environment (dev/test/prod)')
def run_server(port: int, host: str, reload: bool, workers: int, env: str) -> None:
    """
    Run the Nova platform server with the specified configuration.

    Args:
        port: The port number to run the server on
        host: The host address to bind to
        reload: Whether to enable auto-reload for development
        workers: Number of worker processes
        env: The environment to run in (dev/test/prod)
    """
    try:
        # Configure application
        configure_app_settings(env)
        setup_logging(settings)

        # Update settings with command line values
        settings.PORT = port
        settings.HOST = host

        # Print startup information
        print_startup_banner(host, port)

        # Configure Uvicorn
        uvicorn_config = {
            "app": "src.app.main:app",
            "host": settings.HOST,
            "port": settings.PORT,
            "reload": reload,
            "workers": workers,
            "log_config": None,  # Use our custom logger
            "lifespan": "on"
        }

        # Start server
        logger.info(f"Starting server on http://{host}:{port}")
        uvicorn.run(**uvicorn_config)

    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    run_server()