from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str


class LivenessResponse(BaseModel):
    status: str


class ReadinessResponse(BaseModel):
    status: str