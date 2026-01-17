from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_add_success():
    response = client.get("/add?left=2&right=3")
    assert response.status_code == 200
    assert response.json() == {"sum": 5}


def test_add_with_negative_numbers():
    response = client.get("/add?left=-10&right=4")
    assert response.status_code == 200
    assert response.json() == {"sum": -6}


def test_add_with_zero():
    response = client.get("/add?left=0&right=0")
    assert response.status_code == 200
    assert response.json() == {"sum": 0}


def test_add_missing_parameter():
    response = client.get("/add?left=5")
    assert response.status_code == 422


def test_add_invalid_type():
    response = client.get("/add?left=foo&right=3")
    assert response.status_code == 422
