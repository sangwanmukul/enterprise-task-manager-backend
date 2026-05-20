from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.models.task_model import (
    Task
)

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(

    prefix="/api/v1/analytics",

    tags=["Analytics"]
)


@router.get("/")
def analytics(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    total_tasks = db.query(
        Task
    ).count()

    completed_tasks = db.query(
        Task
    ).filter(
        Task.status == "COMPLETED"
    ).count()

    pending_tasks = db.query(
        Task
    ).filter(
        Task.status == "PENDING"
    ).count()

    high_priority_tasks = db.query(
        Task
    ).filter(
        Task.priority == "HIGH"
    ).count()

    return {

        "total_tasks": total_tasks,

        "completed_tasks": completed_tasks,

        "pending_tasks": pending_tasks,

        "high_priority_tasks": high_priority_tasks
    }