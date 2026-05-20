from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.core.database import Base


class ActivityLog(Base):

    __tablename__ = "activity_logs"

    id = Column(
        Integer,
        primary_key=True
    )

    action = Column(String)

    entity_type = Column(String)

    entity_id = Column(Integer)

    performed_by = Column(Integer)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )