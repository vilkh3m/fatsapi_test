from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_show_number():
    response = client.get("/number/42")
    assert response.status_code == 200
    assert response.json() == {"number": 42}

def test_show_number_negative():
    response = client.get("/number/-10")
    assert response.status_code == 200
    assert response.json() == {"number": -10}

def test_show_number_non_integer():
    response = client.get("/number/abc")
    assert response.status_code == 422  # FastAPI should return a validation error

def test_show_datetime():
    response = client.get("/datetime")
    assert response.status_code == 200
    assert "datetime" in response.json()

def test_invalid_endpoint():
    response = client.get("/invalid")
    assert response.status_code == 404
