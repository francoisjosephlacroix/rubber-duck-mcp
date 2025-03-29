import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """Test that the health check endpoint works"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_rubber_duck_endpoint():
    """Test the rubber duck endpoint with valid data"""
    test_data = {
        "code": "def example():\n    print('Hello, World!')",
        "context": "Testing a simple function"
    }
    response = client.post("/tools/rubber-duck", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_rubber_duck_endpoint_no_context():
    """Test the rubber duck endpoint without context"""
    test_data = {
        "code": "def example():\n    print('Hello, World!')"
    }
    response = client.post("/tools/rubber-duck", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"status": "success"}

def test_rubber_duck_endpoint_invalid_data():
    """Test the rubber duck endpoint with invalid data"""
    test_data = {
        "context": "Missing code field"
    }
    response = client.post("/tools/rubber-duck", json=test_data)
    assert response.status_code == 422  # Validation error 