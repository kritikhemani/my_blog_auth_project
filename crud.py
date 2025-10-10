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

# --- Read (R) ---
def get_post_by_slug(session: Session, slug: str) -> Post | None:
    # Use session.scalars for a list of ORM objects, then .first() to get the single object
    stmt = select(Post).where(Post.slug == slug)
    return session.scalars(stmt).first()

# --- Update (U) ---
def update_post_content(session: Session, post_id: int, new_content: str):
    post = session.get(Post, post_id) # Efficiently get by primary key
    if post:
        post.content = new_content
        # 'updated_at' is automatically handled by the model's 'onupdate=datetime.now'
        session.commit()
        return post
    return None

# --- Delete (D) ---
def delete_comment(session: Session, comment_id: int) -> bool:
    # Option 1: Retrieve and delete (ORM object style)
    comment = session.get(Comment, comment_id)
    if comment:
        session.delete(comment)
        session.commit()
        return True
    return False
