from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title : str
    body : str
    class Config:
        from_attributes = True

class Blog(BaseModel):
    title : str
    body : str

    class Config():
        from_attributes = True

class BlogCreate(BlogBase):
    pass

class UserBase(BaseModel):
    name : str
    email : str
    
class UserCreate(UserBase):
    password : str

class UserResponse(UserBase):
    name : str
    email : str
    blogs : List[Blog] = []

    class Config:
        from_attributes = True

class BlogResponse(BlogBase):
    title : str
    body : str

    class Config:
        from_attributes = True   # <- Required in Pydantic v2 to work with ORM

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] | None
