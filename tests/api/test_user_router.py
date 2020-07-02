from typing import Any, List

import pytest
from fastapi import FastAPI
from starlette import status
from starlette.testclient import TestClient

from src.api.api import api_router
from src.api.utils import get_user_services
from src.domain.userManagment.userSchema import UserDBSchema
from src.infrastructure.database.models.user import UserModel


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)

    return app


app = create_test_app()
client = TestClient(app)

USER_MODEL = UserModel(
    user_id=1,
    email="test@test.com",
    full_name="test",
    password="test",
    is_active=True,
    is_superuser=False,
    created_date="1/1/2020",
)


class UserServiceDummy:
    async def create_user(self, user: Any) -> UserModel:
        return USER_MODEL

    async def list_users(self) -> List[UserModel]:
        return [USER_MODEL]

    async def get_user_by_id(self, id: int) -> UserModel:
        return USER_MODEL

    async def update_user(self, id: int, new_user: Any) -> UserModel:
        return USER_MODEL

    async def remove_user(self, id: int) -> UserModel:
        return USER_MODEL


def get_user_services_dummy() -> UserServiceDummy:
    return UserServiceDummy()


app.dependency_overrides[get_user_services] = get_user_services_dummy


@pytest.fixture
def user_model() -> UserModel:
    return USER_MODEL


@pytest.fixture
def user_schema() -> UserDBSchema:
    return UserDBSchema(
        user_id=1,
        email="test@test.com",
        full_name="test",
        is_active=True,
        is_superuser=False,
        created_date="1/1/2020",
    )


class TestUserRouter:
    def test_user_create_valide(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.post(
            "/users/",
            json={
                "email": "test@test.com",
                "full_name": "test",
                "password": "test",
                "is_active": True,
                "is_superuser": False,
                "created_date": "1/1/2020",
            }
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == user_schema.__dict__

    def test_user_update(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.put(
            "/users/1",
            json={
                "email": "test@test.com",
                "full_name": "test",
                "password": "test",
                "is_active": True,
                "is_superuser": False,
                "created_date": "1/1/2020",
            })
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == user_schema.__dict__

    def test_user_delete(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.delete("/users/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == user_schema.__dict__

    def test_user_list_all(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.get("/users/all")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [user_schema.__dict__]

    def test_user_get_byid(
        self, user_model: UserModel, user_schema: UserDBSchema
    ) -> None:

        response = client.get("/users/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == user_schema.__dict__
