import requests

BASE_URL = "http://localhost:8000"
NOTIFY_URL = "http://localhost:8002"
NEWS_URL = "http://localhost:8001"

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

def test_get_user():
    url = f"{BASE_URL}/users/get?email=testuser@example.com"
    response = requests.get(url)
    assert response.status_code == 200
    user = response.json()["user"]
    assert user["email"] == "testuser@example.com"
    assert user["name"] == "Test User"
    assert user["preferences"]["categories"] == ["technology", "science"]
    assert user["preferences"]["technologies"] == ["AI", "ML"]
    assert user["preferences"]["communication_channel"] == "email"

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

def test_fetch_news():
    url = f"{NEWS_URL}/news/fetch?category=technology"
    response = requests.get(url)
    assert response.status_code == 200
    assert "results" in response.json()

def test_summarize_news():
    url = f"{NEWS_URL}/news/summarize?category=technology"
    response = requests.get(url)
    assert response.status_code == 200
    assert "summaries" in response.json()

def test_send_notification():
    url = f"{NOTIFY_URL}/notify/send"
    payload = {
        "email": "testuser@example.com",
        "subject": "Test Notification",
        "message": "This is a test notification."
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Notification sent to testuser@example.com"
