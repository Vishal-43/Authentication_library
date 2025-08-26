import create_db

def login_user(email,password,session):
    user = session.query(create_db.users).filter_by(email=email).first()
    if user is None:
        return [False,'user not found']
    return [True,user]