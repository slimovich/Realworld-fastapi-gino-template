import pytest

from src.domain.userManagment.schema.user import UserCreateSchema, UserDBSchema
from src.domain.userManagment.service.userService import UserService
from src.infrastructure.database.models.user import UserModel

USER_MODEL = UserModel(
                    user_id=1, email="test@test.com", full_name="test", password="test", is_active=True, is_superuser=False, created_date="1/1/2020"
                )

class UserQueriesDummy:
    async def create_user(self, user):
        return USER_MODEL


@pytest.fixture
def user_model() -> UserModel:
    return USER_MODEL


@pytest.fixture
def user_schema() -> UserCreateSchema:
    return UserCreateSchema(
        user_id=1, email="test@test.com", full_name="test", password="test", is_active=True, is_superuser=False, created_date="1/1/2020"
    )


class TestUserService:
    @pytest.mark.asyncio
    async def test_user_create_valide(
        self, user_model: UserModel, user_schema: UserCreateSchema
    ) -> None:
        user_service = UserService(UserQueriesDummy())

        result = await user_service.create_user(user_schema)
        assert result == UserDBSchema(user_id=1, email="test@test.com", full_name="test", is_active=True, is_superuser=False, created_date="1/1/2020")
