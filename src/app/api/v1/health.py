from fastapi import APIRouter
from typing import Dict

router = APIRouter(tags=["Health Check"])

@router.get("/health", summary="Health Check", description="Check if the API is running")
async def health_check() -> Dict:
    return {
        "status": "healthy",
        "message": "Service is running"
    } 