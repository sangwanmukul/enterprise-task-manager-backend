from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text
)

from datetime import datetime

from app.core.database import Base


class Task(Base):

    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(Text)

    status = Column(
        String,
        default="TODO"
    )

    priority = Column(
        String,
        default="MEDIUM"
    )

    estimated_hours = Column(Integer)

    actual_hours = Column(Integer)

    due_date = Column(DateTime)

    assigned_to = Column(
        Integer,
        ForeignKey("users.id")
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )