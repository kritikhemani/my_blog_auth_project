from typing import List
from datetime import datetime
from sqlalchemy import ForeignKey, String, Text, DateTime, Boolean, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base