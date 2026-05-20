from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.task_model import Task

from app.dependencies.auth_dependencies import (
    get_current_user
)

from app.utils.helpers import (
    calculate_completion_rate
)

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    tasks = db.query(Task).all()

    total_tasks = len(tasks)

    completed_tasks = len([
        t for t in tasks
        if t.status == "DONE"
    ])

    pending_tasks = len([
        t for t in tasks
        if t.status != "DONE"
    ])

    overdue_tasks = len([
        t for t in tasks
        if t.status != "DONE"
    ])

    high_priority_tasks = len([
        t for t in tasks
        if t.priority == "HIGH"
    ])

    completion_rate = calculate_completion_rate(
        completed_tasks,
        total_tasks
    )

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "overdue_tasks": overdue_tasks,
        "high_priority_tasks": high_priority_tasks,
        "completion_rate": completion_rate
    }