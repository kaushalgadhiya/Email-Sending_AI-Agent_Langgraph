# modules/send_email.py
from utils.gmail_auth import gmail_login
from email.mime.text import MIMEText
import base64

def create_message(sender: str, to: str, subject: str, message_text: str):
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id: str, message: dict):
    try:
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"✅ Message sent! Message ID: {sent_message['id']}")
        return sent_message
    except Exception as error:
        print(f"❌ An error occurred: {error}")
        return None

def send_email(to: str, subject: str, body: str):
    service = gmail_login()
    user = "me"  # Gmail API uses 'me' to refer to authenticated user
    message = create_message(sender=user, to=to, subject=subject, message_text=body)
    return send_message(service, user, message)

# from  utils import gmail_auth
# from email.mime.text import MIMEText
# import base64


# def create_message(to, subject, body):
#     message = MIMEText(body)
#     message["to"] = to
#     message["subject"] = subject
#     raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
#     return {"raw": raw}


# def send_email(recipient_name, recipient_email, subject, body):
#     try:
#         service = gmail_auth.gmail_login()
#         message = create_message(recipient_email, subject, body)
#         send = service.users().messages().send(userId="me", body=message).execute()
#         return True
#     except Exception as e:
#         print("Error:", e)
#         return False