from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.schemas.project_schema import (
    ProjectCreate,
    AddMemberSchema
)

from app.services.project_service import (
    create_project,
    add_member
)

from app.dependencies.auth_dependencies import (
    get_current_user
)

from app.core.database import get_db

from app.models.project_model import Project

router = APIRouter(
    prefix="/api/v1/projects",
    tags=["Projects"]
)


@router.get("/")
def get_projects(

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return db.query(Project).all()


@router.post("/")
def create_new_project(

    project: ProjectCreate,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return create_project(
        db,
        project,
        current_user.id
    )


@router.post("/{project_id}/members")
def add_project_member(

    project_id: int,

    data: AddMemberSchema,

    db: Session = Depends(get_db),

    current_user=Depends(get_current_user)
):

    return add_member(
        db,
        project_id,
        data.user_id,
        data.role
    )