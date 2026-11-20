from fastapi import APIRouter

from api.schemas.health import (
    HealthResponse,
    LivenessResponse,
    ReadinessResponse,
)

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/", response_model=HealthResponse)
async def health_check():
    return {
        "status": "healthy",
        "service": "agentic-data-engineering-platform",
    }


@router.get("/live", response_model=LivenessResponse)
async def liveness_check():
    return {
        "status": "alive",
    }


@router.get("/ready", response_model=ReadinessResponse)
async def readiness_check():
    return {
        "status": "ready",
    }