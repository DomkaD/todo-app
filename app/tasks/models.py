from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean(), default=False)
    assignee_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    reward = Column(Integer, nullable=False, default=0)
    tags = Column(String, nullable=True)
    due_date = Column(Date, nullable=True)
