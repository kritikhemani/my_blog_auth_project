from typing import List
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey, String, Text, DateTime, Boolean, Table, Column, Index
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
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    posts: Mapped[List["Post"]] = relationship(back_populates="author")
    
    
class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    
class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)