from typing import List, Optional

import inject
from fastapi import APIRouter, HTTPException

from src.domain.userManagment.schema.user import (
    UserCreateSchema,
    UserDBSchema,
    UserUpdateSchema,
)
from src.domain.userManagment.service.userService import UserService

router = APIRouter()


@router.post("/", response_model=UserDBSchema)
async def create_user(user: UserCreateSchema):
    user_service = inject.instance(UserService)
    return await user_service.create_user(user)


@router.get("/all", response_model=List[UserDBSchema])
async def list_users() -> List[UserDBSchema]:
    user_service = inject.instance(UserService)
    users = await user_service.list_users()
    return users


@router.get("/{user_id}", response_model=UserDBSchema)
async def get_user_by_id(user_id: int) -> Optional[UserDBSchema]:
    user_service = inject.instance(UserService)
    user = await user_service.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail=f"User with id:{user_id} not found")


@router.put("/{user_id}", response_model=UserDBSchema)
async def update_user(user_id: int, new_user: UserUpdateSchema) -> UserDBSchema:
    user_service = inject.instance(UserService)
    user_updated = await user_service.update_user(user_id, new_user)
    return user_updated


@router.delete("/{user_id}", response_model=UserDBSchema)
async def remove_user(user_id: int) -> UserDBSchema:
    user_service = inject.instance(UserService)
    user_removed = await user_service.remove_user(user_id)
    return user_removed
