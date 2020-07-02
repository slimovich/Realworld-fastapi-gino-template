from typing import Any, List

import pytest

from src.domain.userManagment.userSchema import UserCreateSchema, UserDBSchema, UserUpdateSchema
from src.domain.userManagment.userService import UserService
from src.infrastructure.database.models.user import UserModel

USER_MODEL = UserModel(
    user_id=1,
    email="test@test.com",
    full_name="test",
    password="test",
    is_active=True,
    is_superuser=False,
    created_date="1/1/2020",
)


class UserQueriesDummy:
    async def create_user(self, user: Any) -> UserModel:
        return USER_MODEL

    async def update_user(self, old_user: Any, new_user: Any) -> UserModel:
        return USER_MODEL

    async def delete_user(self, user_id: int) -> UserModel:
        return USER_MODEL

    async def get_user_byid(self, user_id: int) -> UserModel:
        return USER_MODEL

    async def get_all_users(self) -> List[UserModel]:
        return [USER_MODEL]


@pytest.fixture
def user_model() -> UserModel:
    return USER_MODEL


@pytest.fixture
def user_schema() -> UserCreateSchema:
    return UserCreateSchema(
        user_id=1,
        email="test@test.com",
        full_name="test",
        password="test",
        is_active=True,
        is_superuser=False,
        created_date="1/1/2020",
    )


@pytest.fixture
def user_update_schema() -> UserUpdateSchema:
    return UserUpdateSchema(
        user_id=1,
        email="test@test.com",
        full_name="test",
        password="test",
        is_active=True,
        is_superuser=False,
        created_date="1/1/2020",
    )


class TestUserService:
    @pytest.mark.asyncio
    async def test_user_create_valide(
        self, user_model: UserModel, user_schema: UserCreateSchema
    ) -> None:
        user_service = UserService(UserQueriesDummy())

        result = await user_service.create_user(user_schema)
        assert result == UserDBSchema(
            user_id=1,
            email="test@test.com",
            full_name="test",
            is_active=True,
            is_superuser=False,
            created_date="1/1/2020",
        )

    @pytest.mark.asyncio
    async def test_user_list_users(
        self, user_model: UserModel, user_schema: UserCreateSchema
    ) -> None:
        user_service = UserService(UserQueriesDummy())

        result = await user_service.list_users()
        assert result == [UserDBSchema(
            user_id=1,
            email="test@test.com",
            full_name="test",
            is_active=True,
            is_superuser=False,
            created_date="1/1/2020",
        )]

    @pytest.mark.asyncio
    async def test_user_update_user(
        self, user_model: UserModel, user_update_schema: UserUpdateSchema
    ) -> None:
        user_service = UserService(UserQueriesDummy())

        result = await user_service.update_user(1, user_update_schema)
        assert result == UserDBSchema(
            user_id=1,
            email="test@test.com",
            full_name="test",
            is_active=True,
            is_superuser=False,
            created_date="1/1/2020",
        )

    @pytest.mark.asyncio
    async def test_user_remove_user(
        self, user_model: UserModel, user_schema: UserCreateSchema
    ) -> None:
        user_service = UserService(UserQueriesDummy())

        result = await user_service.remove_user(1)
        assert result == UserDBSchema(
            user_id=1,
            email="test@test.com",
            full_name="test",
            is_active=True,
            is_superuser=False,
            created_date="1/1/2020",
        )

    @pytest.mark.asyncio
    async def test_user_get_user_by_id(
        self, user_model: UserModel, user_schema: UserCreateSchema
    ) -> None:
        user_service = UserService(UserQueriesDummy())

        result = await user_service.get_user_by_id(1)
        assert result == UserDBSchema(
            user_id=1,
            email="test@test.com",
            full_name="test",
            is_active=True,
            is_superuser=False,
            created_date="1/1/2020",
        )
