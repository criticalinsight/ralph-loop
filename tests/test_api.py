from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_info_endpoint():
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert data["app_name"] == "Ralph API"
    assert data["version"] == "1.0.0"
    assert data["status"] == "operational"
    assert data["agent"] == "Ralph"