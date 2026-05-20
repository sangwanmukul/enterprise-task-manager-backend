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

    prefix="/api/v1/ai",

    tags=["AI"]
)


@router.get("/predict-risk/{task_id}")
def predict_risk(

    task_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    task = db.query(
        Task
    ).filter(
        Task.id == task_id
    ).first()

    if not task:

        return {
            "message": "Task not found"
        }

    return {

        "task_id": task.id,

        "title": task.title,

        "risk_score": task.ai_risk_score,

        "priority": task.priority,

        "status": task.status
    }


@router.get("/summary")
def ai_summary(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    tasks = db.query(
        Task
    ).all()

    total = len(tasks)

    high_risk = len([

        t for t in tasks

        if t.ai_risk_score >= 70
    ])

    return {

        "total_tasks": total,

        "high_risk_tasks": high_risk,

        "ai_status": "AI analysis active"
    }