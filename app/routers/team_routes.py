from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.models.team_member_model import (
    TeamMember
)

from app.dependencies.auth_dependencies import (
    get_current_user
)

router = APIRouter(

    prefix="/api/v1/teams",

    tags=["Teams"]
)


@router.get("/")
def get_team_members(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return db.query(
        TeamMember
    ).all()


@router.post("/")
def create_team_member(

    user_id: int,

    project_id: int,

    role: str,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    member = TeamMember(

        user_id=user_id,

        project_id=project_id,

        role=role
    )

    db.add(member)

    db.commit()

    db.refresh(member)

    return member