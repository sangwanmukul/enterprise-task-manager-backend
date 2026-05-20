from sqlalchemy.orm import Session

from app.models.project_model import (
    Project
)

from app.models.team_member_model import (
    TeamMember
)


def create_project(
    db: Session,
    project_data,
    owner_id
):

    project = Project(

        title=project_data.title,

        description=project_data.description,

        owner_id=owner_id
    )

    db.add(project)

    db.commit()

    db.refresh(project)

    return project


def add_member(
    db: Session,
    project_id,
    user_id,
    role
):

    member = TeamMember(

        project_id=project_id,

        user_id=user_id,

        role=role
    )

    db.add(member)

    db.commit()

    db.refresh(member)

    return member