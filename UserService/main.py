from fastapi import FastAPI
from routes import user_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "User Service is up and running"}
