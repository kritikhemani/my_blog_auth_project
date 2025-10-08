# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

# Configuration: Using SQL
DATABASE_URL = "sqlite:///simplified_blog.db"
engine = create_engine(DATABASE_URL, echo=False) 

# Base Class Definition
class Base(DeclarativeBase):
    pass

# Session Utility
def get_session():
    with Session(engine) as session:
        yield session

# Table Creation Function
def create_db_and_tables():
    print("Creating database and tables...")
    Base.metadata.create_all(engine)
    print("Database ready.")