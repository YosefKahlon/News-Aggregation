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