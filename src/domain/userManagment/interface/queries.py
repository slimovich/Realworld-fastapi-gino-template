# used only for python >=3.6
from __future__ import annotations

from abc import abstractmethod
from typing import List, TYPE_CHECKING

from src.domain.userManagment.schema.user import UserCreateSchema, UserDBSchema, UserUpdateSchema
if TYPE_CHECKING:
	from src.infrastructure.database.models.user import UserModel


class IUserQueries:

	@abstractmethod
	async def create_user(self, user: UserCreateSchema) -> UserModel:
		raise NotImplemented

	@abstractmethod
	async def update_user(self, old_user: UserDBSchema, new_user: UserUpdateSchema) -> UserModel:
		raise NotImplemented

	@abstractmethod
	async def delete_user(self, user_id: int) -> UserModel:
		raise NotImplemented

	@abstractmethod
	async def get_user_byid(self, user_id: int) -> UserModel:
		raise NotImplemented

	@abstractmethod
	async def get_all_users(self) -> List[UserModel]:
		raise NotImplemented