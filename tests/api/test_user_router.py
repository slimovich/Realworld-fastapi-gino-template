from typing import Any

import inject
import pytest
from fastapi import FastAPI
from starlette import status
from starlette.testclient import TestClient

from src.api.api import api_router
from src.domain.userManagment.schema.user import UserDBSchema
from src.domain.userManagment.service.userService import UserService
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


@pytest.fixture
def injector() -> None:
    inject.clear_and_configure(
        lambda binder: binder.bind(UserService, UserServiceDummy())  # type: ignore
    )


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
        self, injector: None, user_model: UserModel, user_schema: UserDBSchema
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
            },
        )
        assert response.status_code == status.HTTP_202_ACCEPTED
        assert response.json() == user_schema.__dict__
