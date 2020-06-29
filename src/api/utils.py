from src.domain.userManagment.service.userService import UserService
from src.infrastructure.database.models.user import UserQueries


def get_user_services():
    return UserService(UserQueries())
