from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreateSchema(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdateSchema(UserBase):
    password: Optional[str] = None


# properties to push via API
class UserDBSchema(UserBase):
    user_id: int

    class Config:
        orm_mode = True
