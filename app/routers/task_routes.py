from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File

from sqlalchemy.orm import Session

import shutil
import os

from app.schemas.task_schema import (
    TaskCreate,
    TaskUpdate
)

from app.services.task_service import (
    create_task,
    update_task_status,
    get_tasks,
    soft_delete_task
)

from app.dependencies.auth_dependencies import (
    get_current_user
)

from app.core.database import get_db

from app.models.attachment_model import (
    Attachment
)

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return create_task(
        db,
        task
    )


@router.get("/")
def get_all_tasks(

    page: int = 1,

    limit: int = 10,

    keyword: str = None,

    status: str = None,

    priority: str = None,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return get_tasks(
        db,
        page,
        limit,
        keyword,
        status,
        priority
    )


@router.put("/{task_id}")
def update_task(

    task_id: int,

    task_data: TaskUpdate,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return update_task_status(
        db,
        task_id,
        task_data.status
    )


@router.delete("/{task_id}")
def delete_task(

    task_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return soft_delete_task(
        db,
        task_id
    )


@router.post("/{task_id}/attachments")
def upload_attachment(

    task_id: int,

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    attachment = Attachment(

        file_name=file.filename,

        file_path=file_path,

        task_id=task_id,

        uploaded_by=current_user.id
    )

    db.add(attachment)

    db.commit()

    db.refresh(attachment)

    return attachment