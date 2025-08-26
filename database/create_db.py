import sqlalchemy 

Base = sqlalchemy.orm.declarative_base()


class users(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,unique=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique = True)
    password = sqlalchemy.Column(sqlalchemy.String)


def create_db(db_url):
    engine = sqlalchemy.create_engine(db_url)
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = session()
    return session

def close_session(session):
    session.close()
    return [True,'session closed']




