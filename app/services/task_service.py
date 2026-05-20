from sqlalchemy.orm import Session

from app.models.task_model import Task

from app.services.ai_service import (
    predict_task_risk
)

from app.utils.search import (
    apply_task_search
)

from app.utils.filters import (
    apply_task_filters
)

from app.utils.pagination import (
    paginate
)


def create_task(
    db: Session,
    task_data
):

    risk_score = predict_task_risk(
        task_data.due_date
    )

    task = Task(

        title=task_data.title,

        description=task_data.description,

        priority=task_data.priority,

        assigned_to=task_data.assigned_to,

        project_id=task_data.project_id,

        due_date=task_data.due_date,

        estimated_hours=task_data.estimated_hours,

        ai_risk_score=risk_score
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task


def get_tasks(
    db: Session,
    page: int,
    limit: int,
    keyword=None,
    status=None,
    priority=None
):

    query = db.query(Task).filter(
        Task.is_deleted == False
    )

    query = apply_task_search(
        query,
        keyword,
        Task
    )

    query = apply_task_filters(
        query,
        Task,
        status,
        priority
    )

    return paginate(
        query,
        page,
        limit
    )


def update_task_status(
    db: Session,
    task_id,
    status
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        return {
            "message": "Task not found"
        }

    task.status = status

    db.commit()

    db.refresh(task)

    return task


def soft_delete_task(
    db: Session,
    task_id
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:

        return {
            "message": "Task not found"
        }

    task.is_deleted = True

    db.commit()

    return {
        "message": "Task soft deleted"
    }