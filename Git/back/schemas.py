from pydantic import BaseModel  

class Movie(BaseModel):
    id: int
    tmdb_id: int
    title: str

class Favoritos(BaseModel):
    user_id: str
    tmdb_id: str 
    # title: str

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        form_mode = True

# class UserUpdate(UserBase):
#     id: int
    
#     class Config:
#         form_mode = True