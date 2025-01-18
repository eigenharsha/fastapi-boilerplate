import multiprocessing
from time import time
from typing import Any

from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse

from src.app import template
from src.app.api.v1 import router as v1_router
from src.config.settings import get_settings
from src.core.logger import log_request, logger
from src.core.logging import setup_logging


def is_main_process():
    """Check if this is the main process"""
    return multiprocessing.current_process().name == 'MainProcess'


def create_application(
        app_name: str = "FastAPI App",
        app_description: str = "FastAPI Application",
        **kwargs: Any
) -> FastAPI:
    """Creates a simplified FastAPI application with basic documentation.

    Parameters
    ----------
    router : APIRouter
        The APIRouter object containing the routes
    app_name : str
        Name of the application (default: "FastAPI App")
    app_description : str
        Description of the application (default: "FastAPI Application")
    **kwargs : Any
        Additional keyword arguments for FastAPI

    Returns
    -------
    FastAPI
        Configured FastAPI application instance
    """

    settings = get_settings()

    # Setup logging first
    setup_logging(settings)

    # Update application metadata
    app_config = {
        "title": settings.APP_NAME,
        "description": settings.APP_DESCRIPTION,
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG,
        "docs_url": "/docs" if settings.DOCS_ENABLED else None,
        "redoc_url": "/redoc" if settings.DOCS_ENABLED else None,
        "openapi_url": "/openapi.json" if settings.DOCS_ENABLED else None,
    }

    # Create FastAPI application
    app = FastAPI(**app_config)

    # Add middleware for request logging
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time()
        response = await call_next(request)
        duration = time() - start_time

        await log_request(request, response)
        logger.bind(access=True).debug(f"Request processed in {duration:.2f} seconds")

        return response

    # Add routers
    # Create main router and include versioned routes
    main_router = APIRouter()
    main_router.include_router(v1_router)

    @app.get("/", response_class=HTMLResponse)
    async def root():
        """Root endpoint with modern, professional landing page."""
        return template.landing_page
      

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_methods=settings.CORS_METHODS,
        allow_headers=settings.CORS_HEADERS,
        allow_credentials=True,
    )

    # Include main router
    app.include_router(main_router, prefix=f"/{settings.API_PREFIX}/{settings.API_VERSION}")

    # Create documentation routes
    docs_router = APIRouter()

    @docs_router.get("/docs", include_in_schema=False)
    async def get_swagger_documentation():
        return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

    @docs_router.get("/redoc", include_in_schema=False)
    async def get_redoc_documentation():
        return get_redoc_html(openapi_url="/openapi.json", title="docs")

    @docs_router.get("/openapi.json", include_in_schema=False)
    async def openapi():
        return get_openapi(
            title=app.title,
            version=app.version,
            routes=app.routes
        )

    # Include documentation router
    app.include_router(docs_router)

    # Log only once during initial startup
    # if not app.state.get("logging_initialized"):
    #     print_startup_info(settings)
    #     app.state.logging_initialized = True

    return app
