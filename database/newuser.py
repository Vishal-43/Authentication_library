import create_db
class new_user():
    def create_user(self,email,password,session):

        new_user = create_db.users(email=email,password=password)
        if new_user is None:
            return [False,'failed to create user']
        session.add(new_user)
        session.commit()
        return [True,'user created successfully']

    

