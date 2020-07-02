from src.domain.userManagment.userService import UserService
from src.infrastructure.database.models.user import UserQueries


def get_user_services() -> UserService:
    return UserService(UserQueries())
