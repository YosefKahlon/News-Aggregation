from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from aiocache import cached

notification_router = APIRouter()

class Notification(BaseModel):
    email: EmailStr
    subject: str
    message: str

@notification_router.post("/send")
@cached(ttl=60)  # Cache for 60 seconds
async def send_notification(notification: Notification):
    try:
        send_email(notification.email, notification.subject, notification.message)
        return {"message": f"Notification sent to {notification.email}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def send_email(to_email: str, subject: str, message: str):
    from_email = os.getenv("EMAIL_USER")
    from_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
