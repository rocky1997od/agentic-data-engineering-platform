
from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Agentic Data Engineering Platform is running"
    )


def test_health_endpoint():
    response = client.get("/health/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_liveness_endpoint():
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json()["status"] == "alive"


def test_readiness_endpoint():
    response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ready"
