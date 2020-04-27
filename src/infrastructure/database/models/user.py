from typing import List

from src.core.db import db
from src.domain.userManagment.interface.queries import IUserQueries
from src.domain.userManagment.schema.user import UserCreateSchema, UserUpdateSchema


class UserModel(db.Model):  # type: ignore
    __tablename__ = "user base"

    user_id = db.Column("id", db.Integer, autoincrement=True, primary_key=True)
    email = db.Column("email", db.String, nullable=False, unique=True)
    full_name = db.Column("full_name", db.String)
    password = db.Column("password", db.String)
    is_active = db.Column("is_active", db.Boolean, nullable=False)
    is_superuser = db.Column("is_superuser", db.Boolean, nullable=False)
    created_date = db.Column(
        "created_date", db.DateTime, default=db.func.now(), nullable=False
    )


class UserQueries(IUserQueries):
    async def create_user(self, user: UserCreateSchema) -> UserModel:
        return await UserModel.create(**user.__dict__)

    async def update_user(
        self, old_user: UserModel, new_user: UserUpdateSchema
    ) -> UserModel:
        user_updated = await old_user.update(**new_user.__dict__).apply()
        return user_updated._instance

    async def delete_user(self, user_id: int) -> UserModel:
        return await UserModel.get(user_id).delete()

    async def get_user_byid(self, user_id: int) -> UserModel:
        return await UserModel.get(user_id)

    async def get_all_users(self) -> List[UserModel]:
        return await UserModel.query.gino.all()
