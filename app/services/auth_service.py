from sqlalchemy.orm import Session

from app.models.user_model import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db: Session, user_data):

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(
            user_data.password
        ),
        role=user_data.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    valid = verify_password(
        password,
        user.password
    )

    if not valid:
        return None

    token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return token