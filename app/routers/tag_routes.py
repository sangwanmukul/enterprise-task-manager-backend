from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.tag_model import Tag

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(

    prefix="/api/v1/tags",

    tags=["Tags"]
)


@router.post("/")
def create_tag(

    name: str,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    tag = Tag(
        name=name
    )

    db.add(tag)

    db.commit()

    db.refresh(tag)

    return tag


@router.get("/")
def get_tags(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return db.query(Tag).all()