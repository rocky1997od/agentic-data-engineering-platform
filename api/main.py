from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.routes.health import router as health_router
from api.schemas.error import ErrorResponse
from monitoring.logging.logger import get_logger

logger = get_logger("api")

app = FastAPI(
    title="Agentic Data Engineering Platform",
    description="An agentic platform for monitoring and managing data engineering pipelines.",
    version="1.0.0",
)

app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "message": "Agentic Data Engineering Platform is running"
    }


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        "Unhandled API exception",
        extra={
            "component": "api",
            "pipeline": None,
        },
    )

    error = ErrorResponse(
        status="error",
        message="An unexpected internal error occurred",
        path=request.url.path,
    )

    return JSONResponse(
        status_code=500,
        content=error.model_dump(),
    )

#@app.get("/test-error")
#async def test_error():
#   raise ValueError("Simulated internal failure")