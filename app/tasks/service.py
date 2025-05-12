from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from uuid import UUID
from app.db import DbSession
from app.tasks.models import Task


class TaskService:
    def __init__(self, db_session: DbSession):
        self.db_session = db_session

    async def get_all(self, assignee_id: UUID) -> list[Task]:
        statement = select(Task).where(Task.assignee_id == assignee_id)
        result = await self.db_session.execute(statement)
        return list(result.scalars().all())

    async def create(self, obj: dict) -> Task:
        db_obj = Task(**obj)
        self.db_session.add(db_obj)

        try:
            await self.db_session.commit()
            await self.db_session.refresh(db_obj)
        except SQLAlchemyError as exc:
            await self.db_session.rollback()
            raise exc

        return db_obj

    async def get_total_reward(self) -> int:
        statement = select(Task).where(Task.completed)
        result = await self.db_session.execute(statement)
        return sum([task.reward for task in result.scalars().all()])

    async def update_task_status(self, task_id: int, completed: bool) -> Task:
        statement = select(Task).where(Task.id == task_id)
        result = await self.db_session.execute(statement)
        task = result.scalars().first()

        if task is None:
            raise ValueError(f"Task with id {task_id} does not exist.")

        if task.completed != completed:
            task.completed = completed

        try:
            await self.db_session.commit()
            await self.db_session.refresh(task)
        except SQLAlchemyError:
            await self.db_session.rollback()
            raise

        return task