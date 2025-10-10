from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session
from .models import Base, User, Post, Comment, Tag # Assuming models are in a relative path

# Setup (using SQLite for simplicity)
engine = create_engine("sqlite:///blog_auth.db")
Base.metadata.create_all(engine) # Create table

# --- Create (C) ---
def create_user(session: Session, username: str, email: str, password_hash: str) -> User:
    new_user = User(username=username, email=email, password_hash=password_hash)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
