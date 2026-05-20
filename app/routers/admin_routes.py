from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.user_model import User

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@router.get("/users")
def admin_get_users(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return db.query(User).all()


@router.put("/roles/{user_id}")
def update_role(

    user_id: int,

    role: str,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    user.role = role

    db.commit()

    db.refresh(user)

    return user