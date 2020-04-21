import inject

from typing import List, Optional
from src.domain.userManagment.schema.user import UserCreateSchema, UserDBSchema, UserUpdateSchema
from src.domain.userManagment.interface.queries import IUserQueries

class UserService:

	def __init__(self, userQueries: IUserQueries):
		self.__userQueries = userQueries

	async def create_user(self, user: UserCreateSchema) -> UserDBSchema:
		new_user = await self.__userQueries.create_user(user)
		return UserDBSchema.from_orm(new_user)

	async def list_users(self) -> List[UserDBSchema]:
		users = await self.__userQueries.get_all_users()
		usersSchema = list(map(lambda x: UserDBSchema.from_orm(x), users))
		return usersSchema
	
	async def get_user_by_id(self, user_id: int) -> Optional[UserDBSchema]:
		user = await self.__userQueries.get_user_byid(user_id)
		if user:
			return UserDBSchema.from_orm(user)
		else:
			return None

	async def update_user(self, user_id: int, new_user: UserUpdateSchema) -> UserDBSchema:
		old_user = await self.__userQueries.get_user_byid(user_id)
		userUpdated = await self.__userQueries.update_user(old_user, new_user)
		return UserDBSchema.from_orm(userUpdated)

	async def remove_user(self, user_id: int) -> UserDBSchema:
		userRemoved = await self.__userQueries.delete_user(user_id)
		return UserDBSchema.from_orm(userRemoved)