from typing import Optional
from pydantic import BaseModel, Field
import datetime

class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str

class Post(BaseModel):
    text: str
    posted: datetime
    owner_id: int