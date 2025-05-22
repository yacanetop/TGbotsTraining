from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    age: int

class User(UserBase):
    id: int
    
    class Config:
        orm_mode - True

class Post(BaseModel):
    id: int
    title: str
    body: str
    author: User

class UserCreate(UserBase):
    pass
