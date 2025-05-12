import uuid
from typing import Optional
from app.db import Role
from pydantic import Field
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    first_name: str
    last_name: str
    role: Role
    parent_id: Optional[str] = None


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    role: Role = Field(..., description="Choose 'parent' or 'child'")
    parent_id: Optional[str] = None


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
