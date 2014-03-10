from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from datetime import datetime

ENGINE = None
Session = None
Base = declarative_base()

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

"""this is a fairly non-standard use of python class attributes.
	It's allowed by the language definition, but ultimately, these
	lines we just added are SQLAlchemy specific"""
	## Hey SQLAlchemy! This is class is storing users
	## in a table called.. users(duh!)
class User(Base):
	__tablename__ = "users"
	## Also, can you add a column named id?
	## I am going to store some numbers in here.
	## and so you know, this is going to be the 
	## primary key for my table.
	id = Column(Integer, primary_key = True)
	##SQLAlchemy, this table is optional but i'm
	##Lazy and didn't want to make a new table
	## for new users so when a new user enters an
	##Email then there is a place to stick it, cool? Awesome.
	email = Column(String(64), nullable=True)
	##Same shit down here.. Super optional and 
	##Here due to laziness...You're welcome.
	password = Column(String(64), nullable=True)
	age = Column(Integer, nullable=True)
	zip_code = Column(String(64), nullable=True)
	

class Movies(Base):
	__tablename__ = "movies"
	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable=True)
	released_at = Column(datetime, notnullable=True)
	imdb_url = Column(String(64), nullable=True)

class Rating(Base):
	__tablename__ = "ratings"
	id = Column(Integer, primary_key = True)
	movie_id = Column(Integer, nullable=True)
	user_id = Column(Integer, nullable=True)
	rating = Column(Integer, nullable=True)

### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
