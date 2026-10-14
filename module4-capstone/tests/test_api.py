import pytest
from fastapi.testclient import TestClient
from app.api import app

@pytest.mark.integration
def test_health_and_triage():
    client = TestClient(app)
    assert client.get("/health").json()["status"] == "ok"
    response = client.post("/v1/triage", json={"message":"chest pain", "consent": True})
    assert response.status_code == 200
    assert response.json()["route"] == "emergency"
