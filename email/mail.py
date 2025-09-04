import smtplib
from email.message import EmailMessage
import OTP.opt as O

otp = O.OTP

class EmailManager:
    def __init__(self,smtp_email,smtp_password):
        self.smtp_email = smtp_email
        self.smtp_password = smtp_password

    def send_email(self,email):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.smtp_email, self.smtp_password)
        message = f"""here is your verification code :)
                {otp.generate_otp}
        """
        s.sendmail(self.smtp_email, email, message)
        s.quit()