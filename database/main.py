import create_db
import newuser
import login
import set_2fa

class dbmanager():
    def __init__(self,db_url):
        self.db_url = db_url
        self.session = None

    def create_session(self):
        self.session = create_db.create_db(self.db_url)

    def save_user(self,email,password):
        if self.session is None:
            return [False, 'failed to create session']
        res = newuser.new_user().create_user(email,password,self.session)

        if res[0] is False:
            return res
        
        create_db.close_session(self.session)
        return res
        
    def check_user(self,email,password):
           user = login.login_user(email,password,self.session)
           if user[0] is False:
               return user
           create_db.close_session(self.session)
           return [True,'user found',user[1]]

    def enable_2fa(self,email):
        if self.session is None:
            return [False, 'failed to create session']
        res = set_2fa.enable(email,self.session)
        create_db.close_session(self.session)
        return res