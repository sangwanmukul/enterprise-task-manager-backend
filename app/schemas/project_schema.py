from pydantic import BaseModel


class ProjectCreate(BaseModel):

    title: str

    description: str


class AddMemberSchema(BaseModel):

    user_id: int

    role: str