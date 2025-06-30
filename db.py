from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DB creation
engine = create_engine("sqlite:///Blogs.db", echo=True)

#Session to interact with DB
Session = sessionmaker(bind=engine)

#Base class for all the models
Base = declarative_base()
