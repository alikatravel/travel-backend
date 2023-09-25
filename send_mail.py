import smtplib
from email.message import EmailMessage
import ssl

email_sender = 'alikatraveluz@gmail.com'
email_password = 'nald jaqb yykl nbww'
email_receiver = 'support@alika.uz'
port = 465

subject = 'Test Subject'
body = 'Test message1'

context = ssl.create_default_context()

def send_mail(name, email, body):
    em = EmailMessage()
    em['From'] = f"{name} {email}"
    em['To'] = email_receiver
    em['subject'] = subject
    body = f"""Name: {name}
Email: {email}
Message: {body}"""
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, em.as_string())


send_mail('Javohir', 'example@gmail.com', 'Hey there')