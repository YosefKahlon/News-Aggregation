# News-Aggregation
Personalized News Update Aggregator

## Overview
This project aggregates news and technology updates based on user preferences, fetching the latest news, summarizing it using AI, and sending notifications via email or Telegram.

## Services
- User Service: Manages user registration and preferences.
- Notification Service: Sends notifications via email or Telegram.
- News Aggregator Service: Fetches and summarizes news articles.

## Running the Application
To run the application:

```bash
docker-compose up --build
```

## User Service
### Overview
This service handles user registration, preference management, and user notifications.

### Endpoints

- POST /users/register: Register a new user.
- POST /users/preferences: Set user preferences.
- POST /users/notify: Notify user based on preferences.
- DELETE /users/delete: Delete a user.
- GET /users/get: Retrieve user details.


### Testing the Service
Using Postman

### 1. Register User

- Method: POST
- URL: http://localhost:8000/users/register
- Body: JSON
```json
{
  "email": "testuser@example.com",
  "name": "Test User"
}
```



###  2. Set Preferences

- Method: POST
- URL: http://localhost:8000/users/preferences
- Body: JSON
```json
{
  "email": "testuser@example.com",
  "preferences": {
    "categories": ["technology", "science"],
    "technologies": ["AI", "ML"],
    "communication_channel": "email"
  }
}
```


### 3. Notify User

- Method: POST
- URL: http://localhost:8000/users/notify
- Body: JSON
```json
{
  "email": "testuser@example.com"
}
```


### 4. Delete User

- Method: DELETE
- URL: http://localhost:8000/users/delete?email=testuser@example.com


### 5. Get User

- Method: GET
- URL: http://localhost:8000/users/get?email=testuser@example.com


## Notification Service
### Overview
This service handles sending notifications to users via email.

### Endpoints

- POST /notify/send: Send a notification via email.

### Testing the Service with Postman

- Method: POST
- URL: http://localhost:8002/notify/send
- Body: JSON
- Headers: Content-Type: application/json
```json
{
  "email": "testuser@example.com",
  "subject": "Test Notification",
  "message": "This is a test notification."
}
```

## News Aggregator Service
### Overview
This service fetches and summarizes news articles based on user preferences.

### Endpoints
- GET /news/fetch: Fetch news articles.
- GET /news/summarize: Summarize news articles.


### Testing the Service with Postman
Fetch News
- Method: GET
- URL: http://localhost:8001/news/fetch?category=technology

Summarize News

- Method: GET
- URL: http://localhost:8001/news/summarize?category=technology


## UI Service
### Overview
The UI Service provides a simple web interface to interact with the backend services. It allows users to:
- Register a new user
- Set user preferences for news categories and technologies
- Send notifications to users based on their preferences

### Accessing the UI
```angular2html
http://localhost:5000
```
### Using the UI
#### Register a User:

- Enter an email address and a name in the "Register" section.
- Click the "Register" button.
- A success message will be displayed if the registration is successful. If the user is already registered, an appropriate error message will be shown.
#### Set Preferences:

- Enter the email address of the registered user in the "Set Preferences" section.
- Enter the news categories and technologies of interest (comma-separated).
- Enter the communication channel (e.g., email).
- Click the "Set Preferences" button.
- A success message will be displayed if the preferences are successfully updated. If an error occurs, an appropriate error message will be shown.
#### Notify User:

- Enter the email address of the registered user in the "Notify" section.
- Click the "Notify" button.
- A success message will be displayed if the notification is successfully sent. If an error occurs, an appropriate error message will be shown.


## Environment Variables
```bash
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/news_db?retryWrites=true&w=majority
NEWS_API_KEY=your_news_api_key
GEMINI_API_KEY=your_gemini_api_key
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_email_password
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
```


## Running Integration Tests

### Overview
Integration tests simulate user interaction with the endpoints to ensure the system works as expected.

### Setup
#### Install required libraries
```bash
pip install pytest requests
```

### Running the Tests
```bash
pytest test_integration.py
```


### Testing Caching with Postman
First Request (Uncached):

- Method: GET
- URL: http://localhost:8001/news/fetch?category=technology
- Send the request and note the response time.
- 
Second Request (Cached):

- Immediately after the first request, send the same GET request again.
- Observe the response time.