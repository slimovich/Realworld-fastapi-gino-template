from typing import Any, List, Optional

from src.domain.userManagment.userSchema import UserCreateSchema, UserDBSchema, UserUpdateSchema


class UserService:
    def __init__(self, user_queries: Any):
        self.__user_queries = user_queries

    async def create_user(self, user: UserCreateSchema) -> UserDBSchema:
        new_user = await self.__user_queries.create_user(user)
        return UserDBSchema.from_orm(new_user)

    async def list_users(self) -> List[UserDBSchema]:
        users = await self.__user_queries.get_all_users()
        users_schema = list(map(lambda x: UserDBSchema.from_orm(x), users))
        return users_schema

    async def get_user_by_id(self, user_id: int) -> Optional[UserDBSchema]:
        user = await self.__user_queries.get_user_byid(user_id)
        if user:
            return UserDBSchema.from_orm(user)
        else:
            return None

    async def update_user(self, user_id: int, new_user: UserUpdateSchema) -> UserDBSchema:
        old_user = await self.__user_queries.get_user_byid(user_id)
        user_updated = await self.__user_queries.update_user(old_user, new_user)
        return UserDBSchema.from_orm(user_updated)

    async def remove_user(self, user_id: int) -> UserDBSchema:
        user_removed = await self.__user_queries.delete_user(user_id)
        return UserDBSchema.from_orm(user_removed)
