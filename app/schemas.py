from datetime import datetime
from pydantic import BaseModel


class PostModel(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostModel):
    pass


class PostResponse(PostModel):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
