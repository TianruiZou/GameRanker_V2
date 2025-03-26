from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """
    Test root path
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "welcome to use gamerankerAPI"}

def test_get_leaderboard():
    """
    Test get leaderboard
    """
    response = client.get("/api/leaderboard")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 