import inject
import pytest

from src.domain.userManagment.service.userService import UserService
from src.domain.userManagment.schema.user import UserSchema
from src.infrastructure.database.models.user import UserModel
from src.infrastructure.database.models.user import UserQueries

class UserQueriesDummy:

	async def create_user(self, user):
		return UserModel(pseudo="sss", first_name="aaa", last_name="vvvv", birth_date="zaeaze")


@pytest.fixture
def user_model() -> UserModel:
	return UserModel(pseudo="sss", first_name="aaa", last_name="vvvv", birth_date="zaeaze")

@pytest.fixture
def user_schema() -> UserSchema:
	return UserSchema(pseudo="sss", first_name="aaa", last_name="vvvv", birth_date="zaeaze")


class TestUserService:

	@pytest.mark.asyncio
	async def test_user_create_valide(self, user_model: UserModel, user_schema: UserSchema) -> None:
		user_service = UserService(UserQueriesDummy())

		result = await user_service.create_user(user_schema)
		assert result.__eq__(user_model)