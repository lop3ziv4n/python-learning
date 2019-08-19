# pip3 install sqlAlchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# Insert
session = Session()
user = User()
user.id = 0
user.username = 'Jorge'
session.add(user)
session.commit()

# Select
users = session.query(User).all()
for user in users:
    print('username: {} and id: {}'.format(user.username, user.id))

session.close()
