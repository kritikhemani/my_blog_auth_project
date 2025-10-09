from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, String, Text, DateTime, Boolean, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


post_tag_table = Table(
    'post_tag',
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    posts: Mapped[List["Post"]] = relationship("Post", back_populates="author")