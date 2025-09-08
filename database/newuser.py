import create_db
class new_user():
    def create_user(self,email,password,session):

        new_user = create_db.users(email=email,password=password)
        if new_user is None:
            return [False,'failed to create user']
        session.add(new_user)
        session.commit()
        return [True,'user created successfully']

    def update_email_type(self,email,session):
        user = session.query(create_db.users).filter_by(email=email).first()
        if user is None:
            return [False,'user not found']
        user.email_type = 'verified'
        session.commit()
        return [True,'email verified']

    

