from fastapi import FastAPI
from notifier import notification_router

app = FastAPI()

app.include_router(notification_router, prefix="/notify", tags=["notify"])

@app.get("/")
def read_root():
    return {"message": "Notification Service is up and running"}
