from fastapi.testclient import TestClient
from main import app  # make sure 'main.py' has 'app = FastAPI()'

client = TestClient(app)

def test_book_class():
    response = client.post("/book", json={
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["client_name"] == "Test User"
    assert data["class_id"] == 1
    assert "booking_id" in data
