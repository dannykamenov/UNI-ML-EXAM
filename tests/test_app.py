from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={"data": [[5.1, 3.5, 1.4, 0.2]]})
    assert response.status_code == 200
    assert response.json() == {"prediction": [0]}

def test_predict_invalid_data():
    response = client.post("/predict", json={"data": [[5.1, 3.5, 1.4]]})
    assert response.status_code == 422  # Cannot process the data
