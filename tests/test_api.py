from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_info_endpoint():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"app_name": "Ralph API", "version": "1.0.0"}