import create_db

def change_password(email,password,session):
    user = session.query(create_db.users).filter_by(email=email).first()
    if user is None:
        return [False,'user not found']
    user.password = password
    session.commit()
    return [True,'password changed']