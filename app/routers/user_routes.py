from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.user_model import User

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@router.get("/")
def get_all_users(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return db.query(User).all()


@router.get("/{user_id}")
def get_user(

    user_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return db.query(User).filter(
        User.id == user_id
    ).first()


@router.put("/{user_id}")
def update_user(

    user_id: int,

    name: str,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    user.name = name

    db.commit()

    db.refresh(user)

    return user


@router.delete("/{user_id}")
def delete_user(

    user_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    db.delete(user)

    db.commit()

    return {
        "message": "User deleted"
    }