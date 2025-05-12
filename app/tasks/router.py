from uuid import uuid4
from app.db import DbSession, User, Role
from app.tasks.schemas import TaskRead, TaskCreate
from app.tasks.service import TaskService
from app.users import current_active_user
from fastapi import APIRouter, Depends, HTTPException



router = APIRouter()


@router.get("/")
async def task_list(db_session: DbSession, user: User = Depends(current_active_user)) -> list[TaskRead]:
    task_service = TaskService(db_session)
    print(user)
    tasks = await task_service.get_all(user.id)
    return [TaskRead.model_validate(task) for task in tasks]


@router.post("/")
async def create_task(task: TaskCreate, db_session: DbSession, user: User = Depends(current_active_user)) -> TaskRead:
    print(user.email)
    print(task)
    print(task.model_dump())
    task_service = TaskService(db_session)
    new_task = await task_service.create(task.model_dump())
    return TaskRead.model_validate(new_task)

@router.get("/total-reward")
async def get_total_reward(db_session: DbSession):
    return await TaskService(db_session).get_total_reward()

@router.patch("/{task_id}")
async def update_task_status(
    task_id: int,
    completed: bool,
    db_session: DbSession,
    user: User = Depends(current_active_user)) -> TaskRead:
    task_service = TaskService(db_session)
    updated_task = await task_service.update_task_status(task_id, completed)
    return TaskRead.model_validate(updated_task)

@router.get("/generate-parent-id")
async def generate_parent_id(user: User = Depends(current_active_user)):
    if user.role != Role.PARENT:
        raise HTTPException(status_code=400, detail="Only parents can generate an ID.")
    return {"parent_id": str(uuid4())}