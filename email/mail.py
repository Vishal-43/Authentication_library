import smtplib
from email.message import EmailMessage

class EmailManager:
    def __init__(self,smtp_email,smtp_password):
        self.smtp_email = smtp_email
        self.smtp_password = smtp_password
        
