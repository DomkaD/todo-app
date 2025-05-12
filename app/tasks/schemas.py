from pydantic import BaseModel
from uuid import UUID
from typing import Literal
from datetime import date

class TaskRead(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    assignee_id: UUID
    tags: Literal["work", "personal", "others"]
    reward: int
    due_date: date

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool
    assignee_id: UUID
    tags: Literal["work", "personal", "others"] = "others"
    reward: int
    due_date: date
