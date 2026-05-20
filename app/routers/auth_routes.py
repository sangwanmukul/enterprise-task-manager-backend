from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.schemas.auth_schema import UserSignup

from app.services.auth_service import (
    register_user,
    authenticate_user
)

from app.core.database import get_db

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(
    user: UserSignup,
    db: Session = Depends(get_db)
):

    new_user = register_user(db, user)

    if not new_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User created successfully"
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }