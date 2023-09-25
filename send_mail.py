import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import os

load_dotenv()

EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 0))
EMAIL_RECEIVER = 'support@alika.uz'
context = ssl.create_default_context()


def send_mail(name, email, body):
    em = EmailMessage()
    em['From'] = f"{name} {email}"
    em['To'] = EMAIL_RECEIVER
    body = f"""Name: {name}
Email: {email}
Message: {body}"""
    em.set_content(body)

    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(EMAIL_HOST_USER, EMAIL_RECEIVER, em.as_string())
