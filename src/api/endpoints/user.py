from typing import List, Optional

import inject
from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from src.api.utils import get_user_services
from src.domain.userManagment.schema.user import UserCreateSchema, UserDBSchema, UserUpdateSchema
from src.domain.userManagment.service.userService import UserService

router = APIRouter()


@router.post("/", response_model=UserDBSchema)
async def create_user(user: UserCreateSchema, user_service: UserService = Depends(get_user_services)) -> UserDBSchema:
    return await user_service.create_user(user)


@router.get("/all", response_model=List[UserDBSchema])
async def list_users(user_service: UserService = Depends(get_user_services)) -> List[UserDBSchema]:
    users: List[UserDBSchema] = await user_service.list_users()
    return users


@router.get("/{user_id}", response_model=UserDBSchema)
async def get_user_by_id(user_id: int, user_service: UserService = Depends(get_user_services)) -> Optional[UserDBSchema]:
    user = await user_service.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id:{user_id} not found",
    )


@router.put("/{user_id}", response_model=UserDBSchema)
async def update_user(user_id: int, new_user: UserUpdateSchema, user_service: UserService = Depends(get_user_services)) -> UserDBSchema:
    user_updated: UserDBSchema = await user_service.update_user(user_id, new_user)
    return user_updated


@router.delete("/{user_id}", response_model=UserDBSchema)
async def remove_user(user_id: int, user_service: UserService = Depends(get_user_services)) -> UserDBSchema:
    user_removed: UserDBSchema = await user_service.remove_user(user_id)
    return user_removed
