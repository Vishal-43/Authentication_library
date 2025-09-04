from encrypter import encrypter
from database import main
import email.mail as mail
import OTP.opt as opt
otp = opt.OTP()
import time
mail = mail.EmailManager()
hashpassword = encrypter.hashpassword
db = main.dbmanager()
class signup_manager:
    def __init__(self):
        self.stime = None

    def signup(self,email,password):
        if not email or not password:
            return [False,'email or password missing']
        
        hpass = hashpassword(password)
        signup_manager.send_email(email)
        return db.save_user(email,hpass)
        
    def send_email(self,email):
        mail.send_email(email)
        self.stime = time.time()
        

    def match_otp(self,otp):
        while True:
            if time.time() - self.stime > 600:
                otp.erase_otp()
                self.stime = None
                return [False,'otp expired']
            user_otp = input('enter otp:')
            if mail.otp.verify_otp(user_otp):
                self.stime = None
                return [True,'otp verified']
            else:
                return [False,'invalid OTP']
        

