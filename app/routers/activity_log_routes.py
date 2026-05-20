from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.activity_log_model import (
    ActivityLog
)

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/api/v1/activity-logs",
    tags=["Activity Logs"]
)


@router.get("/")
def get_logs(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return db.query(ActivityLog).all()