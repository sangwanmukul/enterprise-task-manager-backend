from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.schemas.comment_schema import (
    CommentCreate
)

from app.models.comment_model import (
    Comment
)

from app.core.database import (
    get_db
)

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(

    prefix="/api/v1/comments",

    tags=["Comments"]
)


@router.post("/")
def create_comment(

    data: CommentCreate,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    comment = Comment(

        content=data.content,

        task_id=data.task_id,

        user_id=current_user.id
    )

    db.add(comment)

    db.commit()

    db.refresh(comment)

    return comment