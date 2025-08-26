import create_db

def enable(email,session):
    user = session.query(create_db.users).filter_by(email=email).first()
    if user is None:
        return [False,'user not found']
    user.FA = True
    session.commit()
    return [True,'2FA enabled']