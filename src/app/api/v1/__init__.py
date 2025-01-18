from fastapi import APIRouter
from .health import router as health_router

router = APIRouter()

# Include health check route
router.include_router(health_router)
