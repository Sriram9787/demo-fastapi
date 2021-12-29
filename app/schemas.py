from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr


class SendPost(BaseModel):
    title: str
    content: str

class SendUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    user_id: Optional[str] = None