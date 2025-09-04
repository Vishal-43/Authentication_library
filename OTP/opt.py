import secrets

class OTP:
    def __init__(self):
        self.otp = None
        
    def generate_otp(self):
        self.otp = secrets.randbelow(1000000)
        return self.otp
    

    def match_otp(self,otp):
        if not otp or not self.otp:
            return [False,"OTP can not be enpty"]
        
        if self.otp != otp:
            return [False,"otp does not match "]
        
        self.otp = None
        return [True,"Authenticated successfully"]
    
    def erase_otp(self):
        self.otp = None
        