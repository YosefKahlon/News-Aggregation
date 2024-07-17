import requests

BASE_URL = "http://localhost:8000"

def test_register_user():
    url = f"{BASE_URL}/users/register"
    payload = {
        "email": "testuser@example.com",
        "name": "Test User"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

def test_set_preferences():
    url = f"{BASE_URL}/users/preferences"
    payload = {
        "email": "testuser@example.com",
        "preferences": {
            "categories": ["technology", "science"],
            "technologies": ["AI", "ML"],
            "communication_channel": "email"
        }
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Preferences updated successfully"

def test_notify_user():
    url = f"{BASE_URL}/users/notify"
    payload = {
        "email": "testuser@example.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()["message"].startswith("Notification sent to")

def test_delete_user():
    url = f"{BASE_URL}/users/delete?email=testuser@example.com"
    response = requests.delete(url)
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"

def test_get_user():
    url = f"{BASE_URL}/users/get?email=testuser@example.com"
    response = requests.get(url)
    assert response.status_code == 404  # Since user is deleted
    assert response.json()["detail"] == "User not found"
