from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):

    title: str

    description: Optional[str]

    priority: str

    estimated_hours: int

    due_date: datetime

    assigned_to: int

    project_id: int


class TaskUpdate(BaseModel):

    status: str