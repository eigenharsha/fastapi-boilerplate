from enum import Enum
from typing import Any, Dict, Union
from functools import lru_cache
from pathlib import Path
import sys
import logging

from loguru import logger
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

# Mapping between string log levels and logging module constants
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}
#
#
# class InterceptHandler(logging.Handler):
#     """Intercept all logging calls and redirect to loguru"""
#     """
#     Logs to loguru from Python logging.
#     This handler intercepts all standard logging calls and redirects them to loguru
#     while preserving source information (file name, function, line number).
#     """
#
#     def emit(self, record: logging.LogRecord) -> None:
#         # Get corresponding Loguru level if it exists
#         try:
#             level: Union[str, int] = logger.level(record.levelname).name
#         except ValueError:
#             level = record.levelno
#
#         # Find caller from where originated the logged message
#         frame, depth = logging.currentframe(), 2
#         while frame and frame.f_code.co_filename == logging.__file__:
#             frame = frame.f_back
#             depth += 1
#
#         # Extract source information
#         logger.opt(depth=depth, exception=record.exc_info).log(
#             level,
#             record.getMessage()
#         )
#
def setup_logging(settings) -> None:
    """
    Configure logging to intercept all logs and format them through loguru
    """
    # Remove default loguru handler
    logger.remove()

    # Create logs directory if it doesn't exist
    log_path = Path(settings.LOG_PATH)
    log_path.mkdir(parents=True, exist_ok=True)

    # Convert string log level to logging constant
    log_level = LOG_LEVELS.get(settings.LOG_LEVEL.upper(), logging.INFO)
    level_int: int = LOG_LEVELS.get(log_level, logging.INFO)

    # Configure loguru handlers
    logger.add(
        sys.stderr,
        format=settings.LOG_FORMAT,
        level=log_level,
        colorize=True,
        backtrace=True,
        diagnose=True,
        enqueue=True
    )

    # Add file logger
    # File handler
    logger.add(
        str(log_path / settings.LOG_FILENAME),
        format=settings.LOG_FORMAT,
        level=log_level,
        rotation=settings.LOG_ROTATION,
        retention=settings.LOG_RETENTION,
        compression="zip",
        enqueue=True
    )

    # Intercept standard logging
    logging.basicConfig(
        handlers=[InterceptHandler()],
        level=level_int,
        force=True
    )

    # Intercept all other loggers
    for name in logging.root.manager.loggerDict.keys():
        logging_logger = logging.getLogger(name)
        logging_logger.handlers = [InterceptHandler()]
        logging_logger.propagate = False
        logging_logger.level = level_int

    # Explicitly configure uvicorn and fastapi loggers
    loggers = (
        "uvicorn",
        "uvicorn.error",
        "uvicorn.access",
        "fastapi",
        "asyncio"
    )

    for logger_name in loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler()]
        logging_logger.propagate = False
        logging_logger.level = level_int


# Middleware for request logging
async def logging_middleware(request: Request, call_next):
    """Log request and response details"""
    start_time = time.time()

    # Log request
    logger.info(f"Request: {request.method} {request.url}")

    try:
        response = await call_next(request)

        # Log response
        process_time = (time.time() - start_time) * 1000
        logger.info(f"Response: {response.status_code} - Completed in {process_time:.2f}ms")

        return response
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )
class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            "{message}",
            module=record.module,
            func=record.funcName,
            line=record.lineno,
            message=record.getMessage()
        )
