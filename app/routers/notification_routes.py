from fastapi import APIRouter

from fastapi import Depends

from sqlalchemy.orm import Session

from app.models.notification_model import (
    Notification
)

from app.core.database import (
    get_db
)

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(

    prefix="/api/v1/notifications",

    tags=["Notifications"]
)


@router.get("/")
def get_notifications(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    notifications = db.query(
        Notification
    ).filter(

        Notification.user_id == current_user.id

    ).all()

    return notifications