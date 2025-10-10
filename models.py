from typing import List
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey, String, Text, DateTime, Boolean, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Base Class Definition 
class Base(DeclarativeBase):
    pass


class PostTag(Base):
    __tablename__ = 'post_tag',
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), primary_key=True)



class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    posts: Mapped[List["Post"]] = relationship(back_populates="author")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")
    
    
class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True) #  Index 2 (Foreign Key)
    title: Mapped[str] = mapped_column(String(200))
    slug: Mapped[str] = mapped_column(String(250), unique=True, index=True) #  Index 3
    content: Mapped[str] = mapped_column(Text)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    published_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    author: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post", cascade="all, delete-orphan")
    tags: Mapped[List["Tag"]] = relationship(secondary="post_tag", back_populates="posts")
    
    # Composite Index for faster retrieval of published posts
    __table_args__ = (
        Index('idx_published_posts_date', published_at.desc(), is_published), #  Index 4 (Composite)
    )
    
    
class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), index=True) # ⭐ Index 5 (Foreign Key)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True, index=True) # ⭐ Index 6 (Foreign Key)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    post: Mapped["Post"] = relationship(back_populates="comments")
    author: Mapped["User"] = relationship(back_populates="comments") # Can be null for anonymous comments

    
  
class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    slug: Mapped[str] = mapped_column(String(50), unique=True, index=True) # ⭐ Index 7

    posts: Mapped[List["Post"]] = relationship(secondary="post_tag", back_populates="tags")
